from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import ClassVar

import pandas as pd

from models import METRICAS_RED_SOCIAL

from .publicacion_repository import PublicacionRepository


class SQLitePublicacionRepository(PublicacionRepository):
    _instance: ClassVar[SQLitePublicacionRepository | None] = None

    def __new__(cls, db_path: str = "epis_data.db") -> SQLitePublicacionRepository:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, db_path: str = "epis_data.db") -> None:
        if self._initialized:
            return

        self.db_path = Path(db_path)
        self.table_name = "publicaciones"
        self._initialized = True

    @classmethod
    def get_instance(cls, db_path: str = "epis_data.db") -> SQLitePublicacionRepository:
        return cls(db_path)

    def exists_database(self) -> bool:
        return self.db_path.exists()

    def initialize_database(self) -> None:
        with self._connect() as connection:
            connection.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    estudiante TEXT NOT NULL,
                    ciclo TEXT NOT NULL,
                    red_social TEXT NOT NULL,
                    formato TEXT NOT NULL,
                    tipo_alcance TEXT NOT NULL,
                    tipo_interaccion TEXT NOT NULL,
                    detalle_interacciones TEXT NOT NULL,
                    fecha TEXT NOT NULL,
                    alcance INTEGER NOT NULL,
                    interacciones INTEGER NOT NULL
                )
                """
            )
            self._ensure_column(
                connection,
                "tipo_alcance",
                "TEXT NOT NULL DEFAULT 'Alcance'",
            )
            self._ensure_column(
                connection,
                "tipo_interaccion",
                "TEXT NOT NULL DEFAULT 'Interacciones'",
            )
            self._ensure_column(
                connection,
                "detalle_interacciones",
                "TEXT NOT NULL DEFAULT '{}'",
            )
            connection.commit()

    def save_many(self, publicaciones: pd.DataFrame) -> None:
        if publicaciones.empty:
            return

        columnas = [
            "estudiante",
            "ciclo",
            "red_social",
            "formato",
            "tipo_alcance",
            "tipo_interaccion",
            "detalle_interacciones",
            "fecha",
            "alcance",
            "interacciones",
        ]

        data = publicaciones.copy()
        data = self._ensure_metric_columns(data)
        data = data.loc[:, columnas].copy()
        data["fecha"] = pd.to_datetime(data["fecha"]).dt.strftime("%Y-%m-%d")

        with self._connect() as connection:
            data.to_sql(self.table_name, connection, if_exists="append", index=False)

    def clear_all(self) -> None:
        with self._connect() as connection:
            connection.execute(f"DELETE FROM {self.table_name}")
            connection.execute(
                "DELETE FROM sqlite_sequence WHERE name = ?",
                (self.table_name,),
            )
            connection.commit()

    def find_all(self) -> pd.DataFrame:
        return self._read_query(f"SELECT * FROM {self.table_name} ORDER BY fecha")

    def find_by_estudiante(self, estudiante: str) -> pd.DataFrame:
        return self._read_query(
            f"""
            SELECT *
            FROM {self.table_name}
            WHERE estudiante = ?
            ORDER BY fecha
            """,
            params=(estudiante,),
        )

    def get_estudiantes(self) -> list[str]:
        data = self._read_query(
            f"""
            SELECT DISTINCT estudiante
            FROM {self.table_name}
            ORDER BY estudiante
            """
        )
        return data["estudiante"].tolist()

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def _ensure_column(
        self,
        connection: sqlite3.Connection,
        column_name: str,
        definition: str,
    ) -> None:
        columns = {
            row[1]
            for row in connection.execute(f"PRAGMA table_info({self.table_name})")
        }
        if column_name not in columns:
            connection.execute(
                f"ALTER TABLE {self.table_name} ADD COLUMN {column_name} {definition}"
            )

    def _ensure_metric_columns(self, data: pd.DataFrame) -> pd.DataFrame:
        if "tipo_alcance" not in data.columns:
            data["tipo_alcance"] = data["red_social"].map(
                lambda red: METRICAS_RED_SOCIAL.get(str(red), {}).get(
                    "tipo_alcance",
                    "Alcance",
                )
            )

        if "tipo_interaccion" not in data.columns:
            data["tipo_interaccion"] = data["red_social"].map(
                lambda red: METRICAS_RED_SOCIAL.get(str(red), {}).get(
                    "tipo_interaccion",
                    "Interacciones",
                )
            )

        if "detalle_interacciones" not in data.columns:
            data["detalle_interacciones"] = "{}"

        return data

    def _read_query(
        self,
        query: str,
        params: tuple[object, ...] | None = None,
    ) -> pd.DataFrame:
        with self._connect() as connection:
            data = pd.read_sql_query(query, connection, params=params)

        if "fecha" in data.columns:
            data["fecha"] = pd.to_datetime(data["fecha"])

        if {"alcance", "interacciones"}.issubset(data.columns):
            data["engagement_rate"] = data.apply(
                lambda row: 0.0
                if row["alcance"] == 0
                else row["interacciones"] / row["alcance"],
                axis=1,
            )

        return data
