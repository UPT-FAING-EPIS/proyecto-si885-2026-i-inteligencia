from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Publicacion:
    id: int | None
    estudiante: str
    ciclo: str
    red_social: str
    formato: str
    tipo_alcance: str
    tipo_interaccion: str
    detalle_interacciones: str
    fecha: date
    alcance: int
    interacciones: int

    @property
    def engagement_rate(self) -> float:
        if self.alcance == 0:
            return 0.0
        return self.interacciones / self.alcance
