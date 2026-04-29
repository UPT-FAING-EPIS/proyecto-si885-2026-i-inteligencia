import pandas as pd
import pytest

from services import AnalyticsService


class FakePublicacionRepository:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def exists_database(self) -> bool:
        return True

    def initialize_database(self) -> None:
        pass

    def save_many(self, publicaciones: pd.DataFrame) -> None:
        self.data = publicaciones

    def find_all(self) -> pd.DataFrame:
        return self.data.copy()

    def find_by_estudiante(self, estudiante: str) -> pd.DataFrame:
        return self.data[self.data["estudiante"] == estudiante].copy()

    def get_estudiantes(self) -> list[str]:
        return sorted(self.data["estudiante"].unique().tolist())


@pytest.fixture
def publicaciones() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "estudiante": "Ana Perez",
                "ciclo": "VII",
                "red_social": "LinkedIn",
                "formato": "Video",
                "fecha": "2026-01-10",
                "alcance": 100,
                "interacciones": 30,
                "detalle_interacciones": '{"comentarios": 6, "reacciones": 20, "reposts": 4}',
            },
            {
                "estudiante": "Ana Perez",
                "ciclo": "VII",
                "red_social": "LinkedIn",
                "formato": "Texto",
                "fecha": "2026-01-20",
                "alcance": 200,
                "interacciones": 20,
                "detalle_interacciones": '{"comentarios": 4, "reacciones": 12, "reposts": 4}',
            },
            {
                "estudiante": "Ana Perez",
                "ciclo": "VIII",
                "red_social": "Instagram",
                "formato": "Imagen",
                "fecha": "2026-02-10",
                "alcance": 100,
                "interacciones": 15,
                "detalle_interacciones": '{"comentarios": 2, "me_gusta": 13}',
            },
            {
                "estudiante": "Luis Rojas",
                "ciclo": "IX",
                "red_social": "YouTube",
                "formato": "Video",
                "fecha": "2026-02-15",
                "alcance": 100,
                "interacciones": 50,
                "detalle_interacciones": '{"comentarios": 8, "me_gusta": 42}',
            },
        ]
    )


def test_get_metricas_estudiante(publicaciones: pd.DataFrame) -> None:
    service = AnalyticsService(FakePublicacionRepository(publicaciones))

    metricas = service.get_metricas_estudiante("Ana Perez")

    assert metricas == {
        "total_publicaciones": 3,
        "total_interacciones": 65,
        "red_favorita": "LinkedIn",
    }


def test_get_metricas_estudiante_filtra_por_red(publicaciones: pd.DataFrame) -> None:
    service = AnalyticsService(FakePublicacionRepository(publicaciones))

    metricas = service.get_metricas_estudiante(
        "Ana Perez",
        red_social="Instagram",
    )

    assert metricas == {
        "total_publicaciones": 1,
        "total_interacciones": 15,
        "red_favorita": "Instagram",
    }


def test_get_metricas_estudiante_sin_datos(publicaciones: pd.DataFrame) -> None:
    service = AnalyticsService(FakePublicacionRepository(publicaciones))

    metricas = service.get_metricas_estudiante("No Existe")

    assert metricas == {
        "total_publicaciones": 0,
        "total_interacciones": 0,
        "red_favorita": "Sin datos",
    }


def test_get_interacciones_tiempo_agrupa_por_mes(publicaciones: pd.DataFrame) -> None:
    service = AnalyticsService(FakePublicacionRepository(publicaciones))

    data = service.get_interacciones_tiempo("Ana Perez")

    assert data["fecha"].dt.strftime("%Y-%m").tolist() == ["2026-01", "2026-02"]
    assert data["interacciones"].tolist() == [50, 15]


def test_get_interacciones_tiempo_filtra_por_red(publicaciones: pd.DataFrame) -> None:
    service = AnalyticsService(FakePublicacionRepository(publicaciones))

    data = service.get_interacciones_tiempo("Ana Perez", red_social="LinkedIn")

    assert data["fecha"].dt.strftime("%Y-%m").tolist() == ["2026-01"]
    assert data["interacciones"].tolist() == [50]


def test_get_interacciones_por_red_perfil(publicaciones: pd.DataFrame) -> None:
    service = AnalyticsService(FakePublicacionRepository(publicaciones))

    data = service.get_interacciones_por_red(estudiante="Ana Perez")

    assert data["red_social"].tolist() == ["LinkedIn", "Instagram"]
    assert data["interacciones"].tolist() == [50, 15]


def test_get_interacciones_por_red_global_filtrado(publicaciones: pd.DataFrame) -> None:
    service = AnalyticsService(FakePublicacionRepository(publicaciones))

    data = service.get_interacciones_por_red(red_social="YouTube")

    assert data["red_social"].tolist() == ["YouTube"]
    assert data["interacciones"].tolist() == [50]


def test_get_alcance_por_ciclo(publicaciones: pd.DataFrame) -> None:
    service = AnalyticsService(FakePublicacionRepository(publicaciones))

    data = service.get_alcance_por_ciclo()

    assert data["ciclo"].astype(str).tolist() == ["VII", "VIII", "IX"]
    assert data["alcance"].tolist() == [300, 100, 100]


def test_get_alcance_por_ciclo_filtra_por_red(publicaciones: pd.DataFrame) -> None:
    service = AnalyticsService(FakePublicacionRepository(publicaciones))

    data = service.get_alcance_por_ciclo(red_social="LinkedIn")

    assert data["ciclo"].astype(str).tolist() == ["VII"]
    assert data["alcance"].tolist() == [300]


def test_get_top_engagement(publicaciones: pd.DataFrame) -> None:
    service = AnalyticsService(FakePublicacionRepository(publicaciones))

    data = service.get_top_engagement(limit=2)

    assert data["estudiante"].tolist() == ["Luis Rojas", "Ana Perez"]
    assert data.loc[0, "engagement_rate"] == pytest.approx(0.5)
    assert data.loc[1, "engagement_rate"] == pytest.approx(0.1625)


def test_get_top_engagement_filtra_por_red(publicaciones: pd.DataFrame) -> None:
    service = AnalyticsService(FakePublicacionRepository(publicaciones))

    data = service.get_top_engagement(limit=10, red_social="LinkedIn")

    assert data["estudiante"].tolist() == ["Ana Perez"]
    assert data.loc[0, "interacciones"] == 50
    assert data.loc[0, "engagement_rate"] == pytest.approx(50 / 300)


def test_get_contexto_red_retorna_semantica_por_red() -> None:
    service = AnalyticsService(FakePublicacionRepository(pd.DataFrame()))

    contexto = service.get_contexto_red("GitHub")

    assert contexto["tipo_alcance"] == "Vistas tecnicas"
    assert contexto["tipo_interaccion"] == "Pushes, pull requests, issues y stars"
    assert "pushes" in contexto["componentes"]


def test_get_detalle_interacciones_agrupa_componentes(publicaciones: pd.DataFrame) -> None:
    service = AnalyticsService(FakePublicacionRepository(publicaciones))

    data = service.get_detalle_interacciones("Ana Perez", "LinkedIn")

    assert data["componente"].tolist() == ["Reacciones", "Comentarios", "Reposts"]
    assert data["interacciones"].tolist() == [32, 10, 8]


def test_get_detalle_interacciones_no_mezcla_todas_las_redes(
    publicaciones: pd.DataFrame,
) -> None:
    service = AnalyticsService(FakePublicacionRepository(publicaciones))

    data = service.get_detalle_interacciones("Ana Perez")

    assert data.empty
