import pandas as pd

from controllers import AppController, DashboardController


class FakeRepository:
    def __init__(self) -> None:
        self.estudiantes = ["Ana Perez", "Luis Rojas"]

    def exists_database(self) -> bool:
        return True

    def initialize_database(self) -> None:
        pass

    def save_many(self, publicaciones: pd.DataFrame) -> None:
        pass

    def find_all(self) -> pd.DataFrame:
        return pd.DataFrame()

    def find_by_estudiante(self, estudiante: str) -> pd.DataFrame:
        return pd.DataFrame()

    def get_estudiantes(self) -> list[str]:
        return self.estudiantes


class FakeDataService:
    def __init__(self) -> None:
        self.ensure_seed_data_called = False

    def ensure_seed_data(self) -> None:
        self.ensure_seed_data_called = True


class FakeAnalyticsService:
    def __init__(self) -> None:
        self.metricas_estudiante_called_with = None
        self.interacciones_tiempo_called_with = None
        self.interacciones_por_red_called_with = None
        self.top_engagement_limit = None
        self.alcance_red_social = None
        self.top_red_social = None

    def get_metricas_estudiante(
        self,
        estudiante: str,
        red_social: str | None = None,
    ) -> dict[str, int | str]:
        self.metricas_estudiante_called_with = (estudiante, red_social)
        return {
            "total_publicaciones": 3,
            "total_interacciones": 120,
            "red_favorita": "LinkedIn",
        }

    def get_interacciones_tiempo(
        self,
        estudiante: str,
        red_social: str | None = None,
    ) -> pd.DataFrame:
        self.interacciones_tiempo_called_with = (estudiante, red_social)
        return pd.DataFrame(
            {
                "fecha": pd.to_datetime(["2026-01-01"]),
                "interacciones": [120],
            }
        )

    def get_interacciones_por_red(
        self,
        estudiante: str | None = None,
        red_social: str | None = None,
    ) -> pd.DataFrame:
        self.interacciones_por_red_called_with = (estudiante, red_social)
        return pd.DataFrame({"red_social": ["LinkedIn"], "interacciones": [120]})

    def get_alcance_por_ciclo(self, red_social: str | None = None) -> pd.DataFrame:
        self.alcance_red_social = red_social
        return pd.DataFrame({"ciclo": ["VII"], "alcance": [1000]})

    def get_top_engagement(
        self,
        limit: int = 10,
        red_social: str | None = None,
    ) -> pd.DataFrame:
        self.top_engagement_limit = limit
        self.top_red_social = red_social
        return pd.DataFrame(
            {
                "estudiante": ["Ana Perez"],
                "engagement_rate": [0.2],
            }
        )


class FakeView:
    def __init__(
        self,
        selected_view: str = AppController.PERFIL_VIEW,
        selected_student: str | None = "Ana Perez",
    ) -> None:
        self.selected_view = selected_view
        self.selected_student = selected_student
        self.sidebar_estudiantes = []
        self.empty_messages = []
        self.rendered_metricas = None
        self.rendered_line_chart = None
        self.rendered_interacciones_red_chart = None
        self.rendered_bar_chart = None
        self.rendered_top_table = None

    def render_sidebar(
        self,
        estudiantes: list[str],
    ) -> tuple[str, str | None, str | None]:
        self.sidebar_estudiantes = estudiantes
        return self.selected_view, self.selected_student, "LinkedIn"

    def render_empty_state(self, message: str) -> None:
        self.empty_messages.append(message)

    def render_metricas(self, metricas: dict[str, int | str]) -> None:
        self.rendered_metricas = metricas

    def render_line_chart(self, data: pd.DataFrame) -> None:
        self.rendered_line_chart = data

    def render_interacciones_red_chart(self, data: pd.DataFrame) -> None:
        self.rendered_interacciones_red_chart = data

    def render_bar_chart(self, data: pd.DataFrame) -> None:
        self.rendered_bar_chart = data

    def render_top_table(self, data: pd.DataFrame) -> None:
        self.rendered_top_table = data


def build_app_controller(
    selected_view: str = AppController.PERFIL_VIEW,
    selected_student: str | None = "Ana Perez",
) -> tuple[AppController, FakeDataService, FakeAnalyticsService, FakeView]:
    repository = FakeRepository()
    data_service = FakeDataService()
    analytics_service = FakeAnalyticsService()
    view = FakeView(selected_view, selected_student)
    controller = AppController(repository, data_service, analytics_service, view)
    return controller, data_service, analytics_service, view


def test_app_controller_run_inicializa_datos_y_renderiza_perfil() -> None:
    controller, data_service, analytics_service, view = build_app_controller()

    controller.run()

    assert data_service.ensure_seed_data_called is True
    assert view.sidebar_estudiantes == ["Ana Perez", "Luis Rojas"]
    assert analytics_service.metricas_estudiante_called_with == (
        "Ana Perez",
        "LinkedIn",
    )
    assert analytics_service.interacciones_tiempo_called_with == (
        "Ana Perez",
        "LinkedIn",
    )
    assert analytics_service.interacciones_por_red_called_with == (
        "Ana Perez",
        "LinkedIn",
    )
    assert view.rendered_metricas["total_interacciones"] == 120
    assert view.rendered_line_chart is not None
    assert view.rendered_interacciones_red_chart is not None


def test_app_controller_route_renderiza_dashboard_global() -> None:
    controller, _, analytics_service, view = build_app_controller(
        selected_view=AppController.GLOBAL_VIEW,
        selected_student=None,
    )

    controller.run()

    assert analytics_service.top_engagement_limit == 10
    assert analytics_service.alcance_red_social == "LinkedIn"
    assert analytics_service.top_red_social == "LinkedIn"
    assert analytics_service.interacciones_por_red_called_with == (None, "LinkedIn")
    assert view.rendered_bar_chart is not None
    assert view.rendered_interacciones_red_chart is not None
    assert view.rendered_top_table is not None


def test_app_controller_route_muestra_empty_state_si_vista_no_existe() -> None:
    controller, _, _, view = build_app_controller(selected_view="Otra vista")

    controller.run()

    assert view.empty_messages == ["Vista no disponible."]


def test_dashboard_controller_muestra_empty_state_si_no_hay_estudiante() -> None:
    _, _, analytics_service, view = build_app_controller(selected_student=None)
    dashboard_controller = DashboardController(analytics_service, view)

    dashboard_controller.show_perfil_estudiante(None)

    assert view.empty_messages == ["No hay estudiantes disponibles."]
    assert analytics_service.metricas_estudiante_called_with is None
