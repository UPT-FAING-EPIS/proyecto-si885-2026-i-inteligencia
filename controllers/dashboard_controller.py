from __future__ import annotations

from services import AnalyticsService

from .view_protocol import DashboardViewProtocol


class DashboardController:
    def __init__(
        self,
        analytics_service: AnalyticsService,
        view: DashboardViewProtocol,
    ) -> None:
        self.analytics_service = analytics_service
        self.view = view

    def show_perfil_estudiante(
        self,
        estudiante: str | None,
        red_social: str | None = None,
    ) -> None:
        if not estudiante:
            self.view.render_empty_state("No hay estudiantes disponibles.")
            return

        metricas = self.analytics_service.get_metricas_estudiante(
            estudiante,
            red_social=red_social,
        )
        interacciones_tiempo = self.analytics_service.get_interacciones_tiempo(
            estudiante,
            red_social=red_social,
        )
        interacciones_por_red = self.analytics_service.get_interacciones_por_red(
            estudiante=estudiante,
            red_social=red_social,
        )

        self.view.render_metricas(metricas)
        self.view.render_line_chart(interacciones_tiempo)
        self.view.render_interacciones_red_chart(interacciones_por_red)

    def show_impacto_global(self, red_social: str | None = None) -> None:
        alcance_por_ciclo = self.analytics_service.get_alcance_por_ciclo(
            red_social=red_social
        )
        interacciones_por_red = self.analytics_service.get_interacciones_por_red(
            red_social=red_social
        )
        top_engagement = self.analytics_service.get_top_engagement(
            limit=10,
            red_social=red_social,
        )

        self.view.render_bar_chart(alcance_por_ciclo)
        self.view.render_interacciones_red_chart(interacciones_por_red)
        self.view.render_top_table(top_engagement)
