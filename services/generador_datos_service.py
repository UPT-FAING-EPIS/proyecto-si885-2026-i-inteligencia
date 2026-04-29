from __future__ import annotations

import json
from datetime import date
from random import Random

import pandas as pd
from faker import Faker

from models import CICLOS, FORMATOS, METRICAS_RED_SOCIAL, REDES_SOCIALES
from repositories import PublicacionRepository


class GeneradorDatosService:
    CICLOS = CICLOS
    REDES_SOCIALES = REDES_SOCIALES
    FORMATOS = FORMATOS
    METRICAS_RED_SOCIAL = METRICAS_RED_SOCIAL

    def __init__(
        self,
        repository: PublicacionRepository,
        num_registros: int = 1500,
        reference_date: date | None = None,
        seed: int = 42,
    ) -> None:
        self.repository = repository
        self.num_registros = num_registros
        self.reference_date = reference_date or date.today()
        self.random = Random(seed)
        self.faker = Faker("es_ES")
        self.faker.seed_instance(seed)

    def ensure_seed_data(self) -> None:
        database_exists = self.repository.exists_database()
        self.repository.initialize_database()

        current_data = self.repository.find_all()
        if database_exists and self._is_current_seed_data(current_data):
            return

        if not current_data.empty:
            self.repository.clear_all()

        publicaciones = self.generate_publicaciones()
        self.repository.save_many(publicaciones)

    def generate_publicaciones(self) -> pd.DataFrame:
        estudiantes = self._generate_estudiantes()
        registros = []

        for _ in range(self.num_registros):
            estudiante = self.random.choice(estudiantes)
            red_social = self.random.choice(self.REDES_SOCIALES)
            formato = self.random.choice(self.FORMATOS)
            alcance, interacciones, detalle_interacciones = self._calculate_metricas(
                red_social,
                formato,
            )
            metricas_red = self.METRICAS_RED_SOCIAL[red_social]

            registros.append(
                {
                    "estudiante": estudiante["nombre"],
                    "ciclo": estudiante["ciclo"],
                    "red_social": red_social,
                    "formato": formato,
                    "tipo_alcance": metricas_red["tipo_alcance"],
                    "tipo_interaccion": metricas_red["tipo_interaccion"],
                    "detalle_interacciones": json.dumps(
                        detalle_interacciones,
                        ensure_ascii=False,
                        sort_keys=True,
                    ),
                    "fecha": self._generate_fecha_con_picos(),
                    "alcance": alcance,
                    "interacciones": interacciones,
                }
            )

        return pd.DataFrame(registros)

    def _generate_estudiantes(self, cantidad: int = 80) -> list[dict[str, str]]:
        estudiantes = []
        nombres_usados = set()
        ciclo_index = 0

        while len(estudiantes) < cantidad:
            nombre = self.faker.name()
            if nombre in nombres_usados:
                continue

            estudiantes.append(
                {
                    "nombre": nombre,
                    "ciclo": self.CICLOS[ciclo_index % len(self.CICLOS)],
                }
            )
            nombres_usados.add(nombre)
            ciclo_index += 1

        return estudiantes

    def _is_current_seed_data(self, data: pd.DataFrame) -> bool:
        if data.empty:
            return False

        required_columns = {
            "ciclo",
            "red_social",
            "tipo_alcance",
            "tipo_interaccion",
            "detalle_interacciones",
        }
        if not required_columns.issubset(data.columns):
            return False

        ciclos = set(data["ciclo"].dropna().astype(str).unique())
        redes = set(data["red_social"].dropna().astype(str).unique())
        has_empty_detail = (
            data["detalle_interacciones"].dropna().astype(str).eq("{}").any()
        )
        has_expected_labels = all(
            self._row_has_current_metric_labels(row)
            for _, row in data[["red_social", "tipo_alcance", "tipo_interaccion"]]
            .dropna()
            .iterrows()
        )

        return (
            ciclos.issubset(self.CICLOS)
            and redes.issubset(self.REDES_SOCIALES)
            and set(self.REDES_SOCIALES).issubset(redes)
            and not has_empty_detail
            and has_expected_labels
        )

    def _generate_fecha_con_picos(self) -> date:
        months = self._last_12_months()
        weights = [3 if month.month in (7, 12) else 1 for month in months]
        selected_month = self.random.choices(months, weights=weights, k=1)[0]
        days_in_month = pd.Period(
            f"{selected_month.year}-{selected_month.month:02d}"
        ).days_in_month

        day = self.random.randint(1, days_in_month)
        return date(selected_month.year, selected_month.month, day)

    def _calculate_metricas(
        self,
        red_social: str,
        formato: str,
    ) -> tuple[int, int, dict[str, int]]:
        metricas_red = self.METRICAS_RED_SOCIAL[red_social]
        minimo, maximo = metricas_red["alcance_por_formato"][formato]
        alcance = self.random.randint(minimo, maximo)
        variacion = self.random.uniform(0.75, 1.25)
        tasa_interaccion = metricas_red["tasa_interaccion"][formato] * variacion
        interacciones = round(alcance * tasa_interaccion)
        interacciones = min(interacciones, alcance)
        detalle_interacciones = self._distribute_interacciones(
            interacciones,
            metricas_red["componentes"],
        )

        return alcance, interacciones, detalle_interacciones

    def _distribute_interacciones(
        self,
        total: int,
        componentes: dict[str, float],
    ) -> dict[str, int]:
        detalle = {}
        restante = total
        items = list(componentes.items())

        for index, (nombre, peso) in enumerate(items):
            if index == len(items) - 1:
                valor = restante
            else:
                valor = min(restante, round(total * peso))
                restante -= valor

            detalle[nombre] = valor

        return detalle

    def _row_has_current_metric_labels(self, row: pd.Series) -> bool:
        metricas_red = self.METRICAS_RED_SOCIAL.get(str(row["red_social"]))
        if not metricas_red:
            return False

        return (
            row["tipo_alcance"] == metricas_red["tipo_alcance"]
            and row["tipo_interaccion"] == metricas_red["tipo_interaccion"]
        )

    def _last_12_months(self) -> list[date]:
        current_month = date(self.reference_date.year, self.reference_date.month, 1)
        months = []

        for offset in range(11, -1, -1):
            year = current_month.year
            month = current_month.month - offset
            while month <= 0:
                month += 12
                year -= 1

            months.append(date(year, month, 1))

        return months
