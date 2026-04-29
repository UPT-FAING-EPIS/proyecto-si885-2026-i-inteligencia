from __future__ import annotations

from typing import Protocol

import pandas as pd


class DashboardViewProtocol(Protocol):
    def render_sidebar(
        self,
        estudiantes: list[str],
    ) -> tuple[str, str | None, str | None]:
        pass

    def render_empty_state(self, message: str) -> None:
        pass

    def render_metricas(self, metricas: dict[str, int | str]) -> None:
        pass

    def render_line_chart(self, data: pd.DataFrame) -> None:
        pass

    def render_interacciones_red_chart(self, data: pd.DataFrame) -> None:
        pass

    def render_bar_chart(self, data: pd.DataFrame) -> None:
        pass

    def render_top_table(self, data: pd.DataFrame) -> None:
        pass
