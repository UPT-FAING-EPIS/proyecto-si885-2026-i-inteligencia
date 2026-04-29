from datetime import date

import pandas as pd

from services import GeneradorDatosService


class FakePublicacionRepository:
    def __init__(self, database_exists: bool = False, data: pd.DataFrame | None = None):
        self.database_exists = database_exists
        self.data = data if data is not None else pd.DataFrame()
        self.initialized = False
        self.saved_data = pd.DataFrame()
        self.cleared = False

    def exists_database(self) -> bool:
        return self.database_exists

    def initialize_database(self) -> None:
        self.initialized = True

    def save_many(self, publicaciones: pd.DataFrame) -> None:
        self.saved_data = publicaciones.copy()
        self.data = publicaciones.copy()

    def clear_all(self) -> None:
        self.cleared = True
        self.data = pd.DataFrame()

    def find_all(self) -> pd.DataFrame:
        return self.data

    def find_by_estudiante(self, estudiante: str) -> pd.DataFrame:
        return self.data[self.data["estudiante"] == estudiante]

    def get_estudiantes(self) -> list[str]:
        return sorted(self.data["estudiante"].unique().tolist())


def test_generate_publicaciones_crea_columnas_y_cantidad_esperada() -> None:
    service = GeneradorDatosService(
        repository=FakePublicacionRepository(),
        num_registros=150,
        reference_date=date(2026, 4, 24),
        seed=7,
    )

    data = service.generate_publicaciones()

    assert len(data) == 150
    assert data.columns.tolist() == [
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


def test_generate_publicaciones_respeta_reglas_de_negocio() -> None:
    service = GeneradorDatosService(
        repository=FakePublicacionRepository(),
        num_registros=1500,
        reference_date=date(2026, 4, 24),
        seed=42,
    )

    data = service.generate_publicaciones()
    video_promedio = data[data["formato"] == "Video"]["interacciones"].mean()
    texto_promedio = data[data["formato"] == "Texto"]["interacciones"].mean()

    assert (data["interacciones"] <= data["alcance"]).all()
    assert data["detalle_interacciones"].str.startswith("{").all()
    assert video_promedio >= texto_promedio * 1.3


def test_generate_publicaciones_usa_ciclos_y_redes_actuales() -> None:
    service = GeneradorDatosService(
        repository=FakePublicacionRepository(),
        num_registros=1500,
        reference_date=date(2026, 4, 24),
        seed=42,
    )

    data = service.generate_publicaciones()

    assert set(data["ciclo"].unique()).issubset(
        {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"}
    )
    assert {"I", "X"}.issubset(set(data["ciclo"].unique()))
    assert set(data["red_social"].unique()) == {
        "LinkedIn",
        "Instagram",
        "YouTube",
        "GitHub",
    }


def test_generate_publicaciones_usa_ultimos_12_meses_con_picos() -> None:
    service = GeneradorDatosService(
        repository=FakePublicacionRepository(),
        num_registros=1500,
        reference_date=date(2026, 4, 24),
        seed=42,
    )

    data = service.generate_publicaciones()
    meses = pd.to_datetime(data["fecha"]).dt.month
    cantidad_julio = int((meses == 7).sum())
    cantidad_diciembre = int((meses == 12).sum())
    promedio_mensual = len(data) / 12

    assert data["fecha"].min() >= date(2025, 5, 1)
    assert data["fecha"].max() <= date(2026, 4, 30)
    assert cantidad_julio > promedio_mensual
    assert cantidad_diciembre > promedio_mensual


def test_ensure_seed_data_genera_datos_si_no_existen() -> None:
    repository = FakePublicacionRepository(database_exists=False)
    service = GeneradorDatosService(
        repository=repository,
        num_registros=10,
        reference_date=date(2026, 4, 24),
    )

    service.ensure_seed_data()

    assert repository.initialized is True
    assert len(repository.saved_data) == 10


def test_ensure_seed_data_no_duplica_si_la_base_ya_tiene_datos() -> None:
    existing_data = pd.DataFrame(
        [
            {
                "estudiante": f"Estudiante {red}",
                "ciclo": "VII",
                "red_social": red,
                "formato": "Texto",
                "tipo_alcance": {
                    "LinkedIn": "Impresiones profesionales",
                    "Instagram": "Alcance de publicacion",
                    "YouTube": "Visualizaciones",
                    "GitHub": "Vistas tecnicas",
                }[red],
                "tipo_interaccion": {
                    "LinkedIn": "Reacciones, comentarios y reposts",
                    "Instagram": "Me gusta, comentarios, guardados y compartidos",
                    "YouTube": "Me gusta, comentarios y compartidos",
                    "GitHub": "Pushes, pull requests, issues y stars",
                }[red],
                "detalle_interacciones": '{"reacciones": 10}',
                "fecha": date(2026, 4, 1),
                "alcance": 100,
                "interacciones": 10,
            }
            for red in ("LinkedIn", "Instagram", "YouTube", "GitHub")
        ]
    )
    repository = FakePublicacionRepository(database_exists=True, data=existing_data)
    service = GeneradorDatosService(repository=repository, num_registros=10)

    service.ensure_seed_data()

    assert repository.initialized is True
    assert repository.saved_data.empty
    assert repository.cleared is False


def test_ensure_seed_data_regenera_si_encuentra_red_social_obsoleta() -> None:
    old_data = pd.DataFrame(
        [
            {
                "estudiante": "Ana Perez",
                "ciclo": "VII",
                "red_social": "Facebook",
                "formato": "Texto",
                "fecha": date(2026, 4, 1),
                "alcance": 100,
                "interacciones": 10,
            }
        ]
    )
    repository = FakePublicacionRepository(database_exists=True, data=old_data)
    service = GeneradorDatosService(
        repository=repository,
        num_registros=20,
        reference_date=date(2026, 4, 24),
    )

    service.ensure_seed_data()

    assert repository.cleared is True
    assert len(repository.saved_data) == 20
    assert "Facebook" not in repository.saved_data["red_social"].unique()


def test_ensure_seed_data_regenera_si_falta_github() -> None:
    data_sin_github = pd.DataFrame(
        [
            {
                "estudiante": f"Estudiante {red}",
                "ciclo": "VII",
                "red_social": red,
                "formato": "Texto",
                "fecha": date(2026, 4, 1),
                "alcance": 100,
                "interacciones": 10,
            }
            for red in ("LinkedIn", "Instagram", "YouTube")
        ]
    )
    repository = FakePublicacionRepository(database_exists=True, data=data_sin_github)
    service = GeneradorDatosService(
        repository=repository,
        num_registros=1500,
        reference_date=date(2026, 4, 24),
    )

    service.ensure_seed_data()

    assert repository.cleared is True
    assert "GitHub" in repository.saved_data["red_social"].unique()
