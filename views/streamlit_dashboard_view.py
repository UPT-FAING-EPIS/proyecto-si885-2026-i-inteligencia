from __future__ import annotations

from typing import Any

import pandas as pd

from controllers.navigation import GLOBAL_VIEW, NAVIGATION_OPTIONS, PERFIL_VIEW
from models import REDES_SOCIALES, TODAS_LAS_REDES


class StreamlitDashboardView:
    def __init__(self, st_module: Any | None = None, px_module: Any | None = None) -> None:
        if st_module is None:
            import streamlit as st_module

        if px_module is None:
            import plotly.express as px_module

        self.st = st_module
        self.px = px_module

    def configure_page(self) -> None:
        self.st.set_page_config(
            page_title="EPIS Analytics",
            page_icon=":bar_chart:",
            layout="wide",
        )

    def render_sidebar(
        self,
        estudiantes: list[str],
    ) -> tuple[str, str | None, str | None]:
        self.st.sidebar.title("EPIS Analytics")
        view_name = self.st.sidebar.radio("Vista", NAVIGATION_OPTIONS)
        red_option = self.st.sidebar.selectbox(
            "Red social",
            [TODAS_LAS_REDES, *REDES_SOCIALES],
        )
        red_social = None if red_option == TODAS_LAS_REDES else red_option

        estudiante = None
        if view_name == PERFIL_VIEW:
            if estudiantes:
                estudiante = self.st.sidebar.selectbox("Estudiante", estudiantes)
            else:
                self.st.sidebar.info("Sin estudiantes registrados.")

        return view_name, estudiante, red_social

    def render_empty_state(self, message: str) -> None:
        self.st.info(message)

    def render_metricas(self, metricas: dict[str, int | str]) -> None:
        self.st.header("Dashboard Operacional")
        total_publicaciones, total_interacciones, red_favorita = self.st.columns(3)

        total_publicaciones.metric(
            "Publicaciones",
            metricas["total_publicaciones"],
        )
        total_interacciones.metric(
            "Interacciones",
            metricas["total_interacciones"],
        )
        red_favorita.metric(
            "Red favorita",
            metricas["red_favorita"],
        )

    def render_line_chart(self, data: pd.DataFrame) -> None:
        self.st.subheader("Evolución de interacciones")

        if data.empty:
            self.render_empty_state("No hay interacciones para mostrar.")
            return

        fig = self.px.line(
            data,
            x="fecha",
            y="interacciones",
            markers=True,
            title=None,
        )
        fig.update_traces(line_color="#2563eb", marker_color="#2563eb")
        fig.update_layout(
            xaxis_title="Fecha",
            yaxis_title="Interacciones",
            margin={"l": 20, "r": 20, "t": 20, "b": 20},
        )

        self.st.plotly_chart(fig, use_container_width=True)

    def render_interacciones_red_chart(self, data: pd.DataFrame) -> None:
        self.st.subheader("Interacciones por red social")

        if data.empty:
            self.render_empty_state("No hay interacciones por red para mostrar.")
            return

        fig = self.px.bar(
            data,
            x="red_social",
            y="interacciones",
            color="red_social",
            text="interacciones",
            title=None,
        )
        fig.update_traces(textposition="outside")
        fig.update_layout(
            showlegend=False,
            xaxis_title="Red social",
            yaxis_title="Interacciones",
            margin={"l": 20, "r": 20, "t": 20, "b": 20},
        )

        self.st.plotly_chart(fig, use_container_width=True)

    def render_bar_chart(self, data: pd.DataFrame) -> None:
        self.st.header("Dashboard Táctico EPIS")
        self.st.subheader("Alcance por ciclo académico")

        if data.empty:
            self.render_empty_state("No hay alcance para mostrar.")
            return

        fig = self.px.bar(
            data,
            x="ciclo",
            y="alcance",
            color="ciclo",
            text="alcance",
            title=None,
        )
        fig.update_traces(textposition="outside")
        fig.update_layout(
            showlegend=False,
            xaxis_title="Ciclo",
            yaxis_title="Alcance",
            margin={"l": 20, "r": 20, "t": 20, "b": 20},
        )

        self.st.plotly_chart(fig, use_container_width=True)

    def render_top_table(self, data: pd.DataFrame) -> None:
        self.st.subheader("Top 10 estudiantes por engagement")

        if data.empty:
            self.render_empty_state("No hay ranking de engagement para mostrar.")
            return

        table = data.copy()
        if "engagement_rate" in table.columns:
            table["engagement_rate"] = (table["engagement_rate"] * 100).round(2)

        table = table.rename(
            columns={
                "estudiante": "Estudiante",
                "publicaciones": "Publicaciones",
                "alcance": "Alcance",
                "interacciones": "Interacciones",
                "engagement_rate": "Engagement (%)",
            }
        )

        self.st.dataframe(table, use_container_width=True, hide_index=True)
