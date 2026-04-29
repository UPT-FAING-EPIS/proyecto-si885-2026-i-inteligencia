from dataclasses import dataclass


@dataclass(frozen=True)
class Usuario:
    id: int | None
    estudiante: str
    username: str
    password_hash: str
    rol: str = "estudiante"
