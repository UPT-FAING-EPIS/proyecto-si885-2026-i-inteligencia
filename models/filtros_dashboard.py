from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class FiltrosDashboard:
    estudiante: str | None = None
    fecha_inicio: date | None = None
    fecha_fin: date | None = None
    ciclo: str | None = None
    red_social: str | None = None
