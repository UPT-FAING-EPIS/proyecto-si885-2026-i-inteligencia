from __future__ import annotations

from repositories import PublicacionRepository
from services import AnalyticsService, GeneradorDatosService

from .dashboard_controller import DashboardController
from .navigation import GLOBAL_VIEW, PERFIL_VIEW
from .view_protocol import DashboardViewProtocol


class AppController:
    PERFIL_VIEW = PERFIL_VIEW
    GLOBAL_VIEW = GLOBAL_VIEW

    def __init__(
        self,
        repository: PublicacionRepository,
        data_service: GeneradorDatosService,
        analytics_service: AnalyticsService,
        view: DashboardViewProtocol,
    ) -> None:
        self.repository = repository
        self.data_service = data_service
        self.analytics_service = analytics_service
        self.view = view
        self.dashboard_controller = DashboardController(analytics_service, view)

    def bootstrap(self) -> None:
        self.data_service.ensure_seed_data()

    def run(self) -> None:
        self.bootstrap()
        estudiantes = self.repository.get_estudiantes()
        view_name, estudiante, red_social = self.view.render_sidebar(estudiantes)
        self.route(view_name, estudiante, red_social)

    def route(
        self,
        view_name: str,
        estudiante: str | None = None,
        red_social: str | None = None,
    ) -> None:
        if view_name == self.PERFIL_VIEW:
            self.dashboard_controller.show_perfil_estudiante(
                estudiante,
                red_social=red_social,
            )
            return

        if view_name == self.GLOBAL_VIEW:
            self.dashboard_controller.show_impacto_global(red_social=red_social)
            return

        self.view.render_empty_state("Vista no disponible.")
