from pathlib import Path

import pandas as pd
import pytest

from repositories.sqlite_publicacion_repository import SQLitePublicacionRepository


@pytest.fixture(autouse=True)
def reset_singleton() -> None:
    SQLitePublicacionRepository._instance = None
    yield
    SQLitePublicacionRepository._instance = None


@pytest.fixture
def db_path(tmp_path: Path) -> Path:
    return tmp_path / "test_epis_data.db"


@pytest.fixture
def publicaciones() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "estudiante": "Carlos Mendoza",
                "ciclo": "VII",
                "red_social": "LinkedIn",
                "formato": "Video",
                "fecha": "2026-02-15",
                "alcance": 300,
                "interacciones": 90,
            },
            {
                "estudiante": "Ana Perez",
                "ciclo": "IX",
                "red_social": "Instagram",
                "formato": "Imagen",
                "fecha": "2026-01-10",
                "alcance": 150,
                "interacciones": 30,
            },
            {
                "estudiante": "Carlos Mendoza",
                "ciclo": "VII",
                "red_social": "YouTube",
                "formato": "Texto",
                "fecha": "2026-03-20",
                "alcance": 100,
                "interacciones": 10,
            },
        ]
    )


def test_repositorio_singleton_reutiliza_la_misma_instancia(db_path: Path) -> None:
    first = SQLitePublicacionRepository.get_instance(str(db_path))
    second = SQLitePublicacionRepository.get_instance(str(db_path))

    assert first is second


def test_initialize_database_crea_archivo_y_tabla(db_path: Path) -> None:
    repository = SQLitePublicacionRepository.get_instance(str(db_path))

    assert repository.exists_database() is False

    repository.initialize_database()

    assert repository.exists_database() is True
    assert repository.find_all().empty


def test_save_many_y_find_all_retornan_publicaciones_ordenadas(
    db_path: Path,
    publicaciones: pd.DataFrame,
) -> None:
    repository = SQLitePublicacionRepository.get_instance(str(db_path))
    repository.initialize_database()

    repository.save_many(publicaciones)
    data = repository.find_all()

    assert len(data) == 3
    assert data["fecha"].dt.strftime("%Y-%m-%d").tolist() == [
        "2026-01-10",
        "2026-02-15",
        "2026-03-20",
    ]
    assert "engagement_rate" in data.columns
    assert data.loc[0, "engagement_rate"] == pytest.approx(0.2)


def test_find_by_estudiante_filtra_resultados(
    db_path: Path,
    publicaciones: pd.DataFrame,
) -> None:
    repository = SQLitePublicacionRepository.get_instance(str(db_path))
    repository.initialize_database()
    repository.save_many(publicaciones)

    data = repository.find_by_estudiante("Carlos Mendoza")

    assert len(data) == 2
    assert data["estudiante"].unique().tolist() == ["Carlos Mendoza"]
    assert data["fecha"].dt.strftime("%Y-%m-%d").tolist() == [
        "2026-02-15",
        "2026-03-20",
    ]


def test_get_estudiantes_retorna_nombres_ordenados(
    db_path: Path,
    publicaciones: pd.DataFrame,
) -> None:
    repository = SQLitePublicacionRepository.get_instance(str(db_path))
    repository.initialize_database()
    repository.save_many(publicaciones)

    estudiantes = repository.get_estudiantes()

    assert estudiantes == ["Ana Perez", "Carlos Mendoza"]


def test_save_many_ignora_dataframe_vacio(db_path: Path) -> None:
    repository = SQLitePublicacionRepository.get_instance(str(db_path))
    repository.initialize_database()

    repository.save_many(pd.DataFrame())

    assert repository.find_all().empty


def test_clear_all_elimina_publicaciones(
    db_path: Path,
    publicaciones: pd.DataFrame,
) -> None:
    repository = SQLitePublicacionRepository.get_instance(str(db_path))
    repository.initialize_database()
    repository.save_many(publicaciones)

    repository.clear_all()

    assert repository.find_all().empty
