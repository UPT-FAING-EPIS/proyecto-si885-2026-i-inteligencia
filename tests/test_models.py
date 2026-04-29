from datetime import date

from models import FiltrosDashboard, Publicacion


def test_publicacion_calcula_engagement_rate() -> None:
    publicacion = Publicacion(
        id=1,
        estudiante="Ana Perez",
        ciclo="VIII",
        red_social="LinkedIn",
        formato="Video",
        tipo_alcance="Impresiones profesionales",
        tipo_interaccion="Reacciones, comentarios y reposts",
        detalle_interacciones='{"reacciones": 50}',
        fecha=date(2026, 4, 1),
        alcance=200,
        interacciones=50,
    )

    assert publicacion.engagement_rate == 0.25


def test_publicacion_engagement_rate_es_cero_si_no_hay_alcance() -> None:
    publicacion = Publicacion(
        id=1,
        estudiante="Luis Rojas",
        ciclo="IX",
        red_social="Instagram",
        formato="Texto",
        tipo_alcance="Alcance de publicacion",
        tipo_interaccion="Me gusta, comentarios, guardados y compartidos",
        detalle_interacciones='{"me_gusta": 0}',
        fecha=date(2026, 4, 1),
        alcance=0,
        interacciones=0,
    )

    assert publicacion.engagement_rate == 0.0


def test_filtros_dashboard_tiene_valores_opcionales_por_defecto() -> None:
    filtros = FiltrosDashboard()

    assert filtros.estudiante is None
    assert filtros.fecha_inicio is None
    assert filtros.fecha_fin is None
    assert filtros.ciclo is None
    assert filtros.red_social is None
