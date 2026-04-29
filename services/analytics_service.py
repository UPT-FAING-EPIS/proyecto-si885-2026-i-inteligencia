from __future__ import annotations

import json

import pandas as pd

from models import CICLOS, METRICAS_RED_SOCIAL, TODAS_LAS_REDES
from repositories import PublicacionRepository


class AnalyticsService:
    CICLO_ORDER = list(CICLOS)

    def __init__(self, repository: PublicacionRepository) -> None:
        self.repository = repository

    def get_metricas_estudiante(
        self,
        estudiante: str,
        red_social: str | None = None,
    ) -> dict[str, int | str]:
        data = self.repository.find_by_estudiante(estudiante)
        data = self._filter_by_red_social(data, red_social)

        if data.empty:
            return {
                "total_publicaciones": 0,
                "total_interacciones": 0,
                "red_favorita": "Sin datos",
            }

        red_favorita = data["red_social"].value_counts().idxmax()

        return {
            "total_publicaciones": int(len(data)),
            "total_interacciones": int(data["interacciones"].sum()),
            "red_favorita": str(red_favorita),
        }

    def get_interacciones_tiempo(
        self,
        estudiante: str,
        red_social: str | None = None,
    ) -> pd.DataFrame:
        data = self.repository.find_by_estudiante(estudiante)
        data = self._filter_by_red_social(data, red_social)
        if data.empty:
            return pd.DataFrame(columns=["fecha", "interacciones"])

        data = data.copy()
        data["fecha"] = pd.to_datetime(data["fecha"])
        data["fecha"] = data["fecha"].dt.to_period("M").dt.to_timestamp()

        return (
            data.groupby("fecha", as_index=False)["interacciones"]
            .sum()
            .sort_values("fecha")
        )

    def get_interacciones_por_red(
        self,
        estudiante: str | None = None,
        red_social: str | None = None,
    ) -> pd.DataFrame:
        data = (
            self.repository.find_by_estudiante(estudiante)
            if estudiante
            else self.repository.find_all()
        )
        data = self._filter_by_red_social(data, red_social)

        if data.empty:
            return pd.DataFrame(columns=["red_social", "interacciones"])

        return (
            data.groupby("red_social", as_index=False)["interacciones"]
            .sum()
            .sort_values("interacciones", ascending=False)
            .reset_index(drop=True)
        )

    def get_alcance_por_ciclo(self, red_social: str | None = None) -> pd.DataFrame:
        data = self.repository.find_all()
        data = self._filter_by_red_social(data, red_social)
        if data.empty:
            return pd.DataFrame(columns=["ciclo", "alcance"])

        alcance = data.groupby("ciclo", as_index=False)["alcance"].sum()
        alcance["ciclo"] = pd.Categorical(
            alcance["ciclo"],
            categories=self.CICLO_ORDER,
            ordered=True,
        )

        return alcance.sort_values("ciclo").reset_index(drop=True)

    def get_top_engagement(
        self,
        limit: int = 10,
        red_social: str | None = None,
    ) -> pd.DataFrame:
        data = self.repository.find_all()
        data = self._filter_by_red_social(data, red_social)
        if data.empty:
            return pd.DataFrame(
                columns=[
                    "estudiante",
                    "publicaciones",
                    "alcance",
                    "interacciones",
                    "engagement_rate",
                ]
            )

        top = (
            data.groupby("estudiante", as_index=False)
            .agg(
                publicaciones=("estudiante", "size"),
                alcance=("alcance", "sum"),
                interacciones=("interacciones", "sum"),
            )
        )
        top["engagement_rate"] = top.apply(
            lambda row: 0.0
            if row["alcance"] == 0
            else row["interacciones"] / row["alcance"],
            axis=1,
        )

        return (
            top.sort_values(
                ["engagement_rate", "interacciones"],
                ascending=[False, False],
            )
            .head(limit)
            .reset_index(drop=True)
        )

    def get_contexto_red(self, red_social: str | None = None) -> dict[str, object]:
        if not red_social:
            return {
                "red_social": TODAS_LAS_REDES,
                "tipo_alcance": "Alcance agregado",
                "tipo_interaccion": "Interacciones equivalentes",
                "componentes": [
                    "reacciones",
                    "comentarios",
                    "visualizaciones",
                    "aportes",
                ],
            }

        metricas_red = METRICAS_RED_SOCIAL[red_social]
        return {
            "red_social": red_social,
            "tipo_alcance": metricas_red["tipo_alcance"],
            "tipo_interaccion": metricas_red["tipo_interaccion"],
            "componentes": list(metricas_red["componentes"].keys()),
        }

    def get_detalle_interacciones(
        self,
        estudiante: str | None = None,
        red_social: str | None = None,
    ) -> pd.DataFrame:
        if not red_social:
            return pd.DataFrame(columns=["componente", "interacciones"])

        data = (
            self.repository.find_by_estudiante(estudiante)
            if estudiante
            else self.repository.find_all()
        )
        data = self._filter_by_red_social(data, red_social)

        if data.empty or "detalle_interacciones" not in data.columns:
            return pd.DataFrame(columns=["componente", "interacciones"])

        acumulado: dict[str, int] = {}
        for raw_detail in data["detalle_interacciones"].dropna():
            detail = self._parse_detalle_interacciones(str(raw_detail))
            for componente, cantidad in detail.items():
                acumulado[componente] = acumulado.get(componente, 0) + cantidad

        if not acumulado:
            return pd.DataFrame(columns=["componente", "interacciones"])

        return (
            pd.DataFrame(
                [
                    {
                        "componente": self._format_component_name(componente),
                        "interacciones": interacciones,
                    }
                    for componente, interacciones in acumulado.items()
                ]
            )
            .sort_values("interacciones", ascending=False)
            .reset_index(drop=True)
        )

    def _filter_by_red_social(
        self,
        data: pd.DataFrame,
        red_social: str | None,
    ) -> pd.DataFrame:
        if data.empty or not red_social:
            return data

        return data[data["red_social"] == red_social].copy()

    def _parse_detalle_interacciones(self, raw_detail: str) -> dict[str, int]:
        try:
            detail = json.loads(raw_detail)
        except json.JSONDecodeError:
            return {}

        if not isinstance(detail, dict):
            return {}

        return {
            str(componente): int(cantidad)
            for componente, cantidad in detail.items()
            if isinstance(cantidad, int | float)
        }

    def _format_component_name(self, componente: str) -> str:
        return componente.replace("_", " ").capitalize()
