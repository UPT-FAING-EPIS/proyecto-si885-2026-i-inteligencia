from abc import ABC, abstractmethod

from models import Usuario


class UsuarioRepository(ABC):
    @abstractmethod
    def initialize_database(self) -> None:
        pass

    @abstractmethod
    def count_users(self) -> int:
        pass

    @abstractmethod
    def save_many(self, usuarios: list[Usuario]) -> None:
        pass

    @abstractmethod
    def clear_all(self) -> None:
        pass

    @abstractmethod
    def find_by_username(self, username: str) -> Usuario | None:
        pass

    @abstractmethod
    def get_usernames(self) -> list[str]:
        pass
