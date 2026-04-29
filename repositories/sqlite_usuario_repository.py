from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import ClassVar

from models import Usuario

from .usuario_repository import UsuarioRepository


class SQLiteUsuarioRepository(UsuarioRepository):
    _instances: ClassVar[dict[str, SQLiteUsuarioRepository]] = {}

    def __new__(cls, db_path: str = "epis_data.db") -> SQLiteUsuarioRepository:
        key = str(Path(db_path))
        if key not in cls._instances:
            instance = super().__new__(cls)
            instance._initialized = False
            cls._instances[key] = instance
        return cls._instances[key]

    def __init__(self, db_path: str = "epis_data.db") -> None:
        if self._initialized:
            return

        self.db_path = Path(db_path)
        self.table_name = "usuarios"
        self._initialized = True

    @classmethod
    def get_instance(cls, db_path: str = "epis_data.db") -> SQLiteUsuarioRepository:
        return cls(db_path)

    def initialize_database(self) -> None:
        with self._connect() as connection:
            connection.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    estudiante TEXT NOT NULL,
                    username TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL,
                    rol TEXT NOT NULL DEFAULT 'estudiante'
                )
                """
            )
            connection.commit()

    def count_users(self) -> int:
        with self._connect() as connection:
            result = connection.execute(
                f"SELECT COUNT(*) FROM {self.table_name}"
            ).fetchone()
        return int(result[0])

    def save_many(self, usuarios: list[Usuario]) -> None:
        if not usuarios:
            return

        rows = [
            (
                usuario.estudiante,
                usuario.username,
                usuario.password_hash,
                usuario.rol,
            )
            for usuario in usuarios
        ]

        with self._connect() as connection:
            connection.executemany(
                f"""
                INSERT OR IGNORE INTO {self.table_name}
                    (estudiante, username, password_hash, rol)
                VALUES (?, ?, ?, ?)
                """,
                rows,
            )
            connection.commit()

    def clear_all(self) -> None:
        with self._connect() as connection:
            connection.execute(f"DELETE FROM {self.table_name}")
            connection.execute(
                "DELETE FROM sqlite_sequence WHERE name = ?",
                (self.table_name,),
            )
            connection.commit()

    def find_by_username(self, username: str) -> Usuario | None:
        with self._connect() as connection:
            row = connection.execute(
                f"""
                SELECT id, estudiante, username, password_hash, rol
                FROM {self.table_name}
                WHERE lower(username) = lower(?)
                """,
                (username,),
            ).fetchone()

        if row is None:
            return None

        return Usuario(
            id=row[0],
            estudiante=row[1],
            username=row[2],
            password_hash=row[3],
            rol=row[4],
        )

    def get_usernames(self) -> list[str]:
        with self._connect() as connection:
            rows = connection.execute(
                f"SELECT username FROM {self.table_name} ORDER BY username"
            ).fetchall()

        return [row[0] for row in rows]

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)
