from __future__ import annotations

from models import Usuario
from services import AuthService


class FakePublicacionRepository:
    def __init__(self) -> None:
        self.estudiantes = ["Ana Perez", "Luis Rojas"]

    def get_estudiantes(self) -> list[str]:
        return self.estudiantes


class FakeUsuarioRepository:
    def __init__(self, usuarios: list[Usuario] | None = None) -> None:
        self.usuarios = usuarios or []
        self.was_cleared = False

    def initialize_database(self) -> None:
        pass

    def count_users(self) -> int:
        return len(self.usuarios)

    def save_many(self, usuarios: list[Usuario]) -> None:
        self.usuarios.extend(usuarios)

    def clear_all(self) -> None:
        self.was_cleared = True
        self.usuarios = []

    def find_by_username(self, username: str) -> Usuario | None:
        return next(
            (
                usuario
                for usuario in self.usuarios
                if usuario.username.lower() == username.lower()
            ),
            None,
        )

    def get_usernames(self) -> list[str]:
        return sorted(usuario.username for usuario in self.usuarios)


def test_ensure_demo_users_crea_codigos_universitarios() -> None:
    usuario_repository = FakeUsuarioRepository()
    service = AuthService(
        publicacion_repository=FakePublicacionRepository(),
        usuario_repository=usuario_repository,
    )

    service.ensure_demo_users()

    assert [usuario.username for usuario in usuario_repository.usuarios] == [
        "20260001",
        "20260002",
    ]
    assert [usuario.estudiante for usuario in usuario_repository.usuarios] == [
        "Ana Perez",
        "Luis Rojas",
    ]
    assert all(
        usuario.password_hash != AuthService.DEFAULT_PASSWORD
        for usuario in usuario_repository.usuarios
    )


def test_ensure_demo_users_reemplaza_usuarios_legacy() -> None:
    usuario_repository = FakeUsuarioRepository(
        [
            Usuario(
                id=1,
                estudiante="Ana Perez",
                username="Ana Perez",
                password_hash="legacy",
            )
        ]
    )
    service = AuthService(
        publicacion_repository=FakePublicacionRepository(),
        usuario_repository=usuario_repository,
    )

    service.ensure_demo_users()

    assert usuario_repository.was_cleared is True
    assert [usuario.username for usuario in usuario_repository.usuarios] == [
        "20260001",
        "20260002",
    ]
