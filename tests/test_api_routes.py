import pandas as pd
import pytest
from fastapi.testclient import TestClient

from api.dependencies import get_analytics_service, get_auth_service, get_repository
from api.main import app


class FakeRepository:
    def __init__(self) -> None:
        self.estudiantes = ["Ana Perez", "Luis Rojas"]

    def exists_database(self) -> bool:
        return True

    def initialize_database(self) -> None:
        pass

    def save_many(self, publicaciones: pd.DataFrame) -> None:
        pass

    def clear_all(self) -> None:
        pass

    def find_all(self) -> pd.DataFrame:
        return pd.DataFrame()

    def find_by_estudiante(self, estudiante: str) -> pd.DataFrame:
        return pd.DataFrame()

    def get_estudiantes(self) -> list[str]:
        return self.estudiantes


class FakeAuthService:
    def login(self, username: str, password: str) -> dict[str, str | bool]:
        is_authenticated = username == "20260001" and password == "epis123"
        return {
            "estudiante": "Ana Perez" if is_authenticated else username,
            "display_name": "Ana Perez" if is_authenticated else username,
            "username": username,
            "access_token": "valid-token" if is_authenticated else "",
            "token_type": "bearer",
            "is_authenticated": is_authenticated,
        }

    def verify_token(self, token: str) -> dict[str, str]:
        if token != "valid-token":
            raise ValueError("Token invalido.")

        return {
            "estudiante": "Ana Perez",
            "username": "20260001",
            "rol": "estudiante",
        }


class FakeAnalyticsService:
    def get_metricas_estudiante(
        self,
        estudiante: str,
        red_social: str | None = None,
    ) -> dict[str, int | str]:
        return {
            "total_publicaciones": 2,
            "total_interacciones": 80,
            "red_favorita": red_social or "LinkedIn",
        }

    def get_interacciones_tiempo(
        self,
        estudiante: str,
        red_social: str | None = None,
    ) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "fecha": pd.to_datetime(["2026-01-01"]),
                "interacciones": [80],
            }
        )

    def get_interacciones_por_red(
        self,
        estudiante: str | None = None,
        red_social: str | None = None,
    ) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "red_social": [red_social or "LinkedIn"],
                "interacciones": [80],
            }
        )

    def get_detalle_interacciones(
        self,
        estudiante: str | None = None,
        red_social: str | None = None,
    ) -> pd.DataFrame:
        if red_social is None:
            return pd.DataFrame(columns=["componente", "interacciones"])

        return pd.DataFrame(
            {
                "componente": ["Me gusta", "Comentarios"],
                "interacciones": [50, 30],
            }
        )

    def get_alcance_por_ciclo(self, red_social: str | None = None) -> pd.DataFrame:
        return pd.DataFrame({"ciclo": ["I"], "alcance": [1000]})

    def get_top_engagement(
        self,
        limit: int = 10,
        red_social: str | None = None,
    ) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "estudiante": ["Ana Perez"],
                "publicaciones": [2],
                "alcance": [1000],
                "interacciones": [80],
                "engagement_rate": [0.08],
            }
        )

    def get_contexto_red(self, red_social: str | None = None) -> dict[str, object]:
        return {
            "red_social": red_social or "Todas",
            "tipo_alcance": "Visualizaciones"
            if red_social == "YouTube"
            else "Alcance agregado",
            "tipo_interaccion": "Me gusta, comentarios y compartidos"
            if red_social == "YouTube"
            else "Interacciones equivalentes",
            "componentes": ["me_gusta", "comentarios"],
        }


@pytest.fixture
def client() -> TestClient:
    app.dependency_overrides[get_repository] = lambda: FakeRepository()
    app.dependency_overrides[get_auth_service] = lambda: FakeAuthService()
    app.dependency_overrides[get_analytics_service] = lambda: FakeAnalyticsService()

    yield TestClient(app)

    app.dependency_overrides.clear()


def test_health_check(client: TestClient) -> None:
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_estudiantes(client: TestClient) -> None:
    response = client.get("/api/estudiantes")

    assert response.status_code == 200
    assert response.json() == ["Ana Perez", "Luis Rojas"]


def auth_headers() -> dict[str, str]:
    return {"Authorization": "Bearer valid-token"}


def test_login_correcto(client: TestClient) -> None:
    response = client.post(
        "/api/auth/login",
        json={"username": "20260001", "password": "epis123"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "estudiante": "Ana Perez",
        "display_name": "Ana Perez",
        "username": "20260001",
        "access_token": "valid-token",
        "token_type": "bearer",
        "is_authenticated": True,
    }


def test_login_rechaza_credenciales_invalidas(client: TestClient) -> None:
    response = client.post(
        "/api/auth/login",
        json={"username": "20260001", "password": "mal"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Credenciales invalidas."


def test_me_retorna_sesion(client: TestClient) -> None:
    response = client.get("/api/auth/me", headers=auth_headers())

    assert response.status_code == 200
    assert response.json()["estudiante"] == "Ana Perez"


def test_get_perfil_retorna_metricas_y_series(client: TestClient) -> None:
    response = client.get(
        "/api/dashboard/perfil",
        params={"estudiante": "Ana Perez", "red_social": "YouTube"},
        headers=auth_headers(),
    )

    data = response.json()

    assert response.status_code == 200
    assert data["metricas"]["red_favorita"] == "YouTube"
    assert data["interacciones_tiempo"] == [
        {"fecha": "2026-01-01", "interacciones": 80}
    ]
    assert data["interacciones_por_red"] == [
        {"red_social": "YouTube", "interacciones": 80}
    ]
    assert data["detalle_interacciones"] == [
        {"componente": "Me gusta", "interacciones": 50},
        {"componente": "Comentarios", "interacciones": 30},
    ]
    assert data["contexto_red"]["tipo_alcance"] == "Visualizaciones"


def test_get_perfil_rechaza_red_invalida(client: TestClient) -> None:
    response = client.get(
        "/api/dashboard/perfil",
        params={"estudiante": "Ana Perez", "red_social": "TikTok"},
        headers=auth_headers(),
    )

    assert response.status_code == 400


def test_get_perfil_requiere_token(client: TestClient) -> None:
    response = client.get(
        "/api/dashboard/perfil",
        params={"estudiante": "Ana Perez"},
    )

    assert response.status_code == 401


def test_get_global_retorna_agregados(client: TestClient) -> None:
    response = client.get(
        "/api/dashboard/global",
        params={"red_social": "LinkedIn"},
        headers=auth_headers(),
    )

    data = response.json()

    assert response.status_code == 200
    assert data["alcance_por_ciclo"] == [{"ciclo": "I", "alcance": 1000}]
    assert data["interacciones_por_red"] == [
        {"red_social": "LinkedIn", "interacciones": 80}
    ]
    assert data["detalle_interacciones"][0]["componente"] == "Me gusta"
    assert data["top_engagement"][0]["estudiante"] == "Ana Perez"
    assert data["contexto_red"]["red_social"] == "LinkedIn"
