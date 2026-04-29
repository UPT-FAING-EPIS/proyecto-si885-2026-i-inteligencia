from abc import ABC, abstractmethod

import pandas as pd


class PublicacionRepository(ABC):
    @abstractmethod
    def exists_database(self) -> bool:
        pass

    @abstractmethod
    def initialize_database(self) -> None:
        pass

    @abstractmethod
    def save_many(self, publicaciones: pd.DataFrame) -> None:
        pass

    @abstractmethod
    def clear_all(self) -> None:
        pass

    @abstractmethod
    def find_all(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def find_by_estudiante(self, estudiante: str) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_estudiantes(self) -> list[str]:
        pass
