CICLOS = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X")
REDES_SOCIALES = ("LinkedIn", "Instagram", "YouTube", "GitHub")
FORMATOS = ("Video", "Imagen", "Texto")
TODAS_LAS_REDES = "Todas"

METRICAS_RED_SOCIAL = {
    "LinkedIn": {
        "tipo_alcance": "Impresiones profesionales",
        "tipo_interaccion": "Reacciones, comentarios y reposts",
        "componentes": {
            "reacciones": 0.50,
            "comentarios": 0.22,
            "reposts": 0.16,
            "clics_perfil": 0.12,
        },
        "alcance_por_formato": {
            "Texto": (120, 900),
            "Imagen": (180, 1200),
            "Video": (260, 1600),
        },
        "tasa_interaccion": {
            "Texto": 0.075,
            "Imagen": 0.090,
            "Video": 0.110,
        },
    },
    "Instagram": {
        "tipo_alcance": "Alcance de publicacion",
        "tipo_interaccion": "Me gusta, comentarios, guardados y compartidos",
        "componentes": {
            "me_gusta": 0.62,
            "comentarios": 0.14,
            "guardados": 0.14,
            "compartidos": 0.10,
        },
        "alcance_por_formato": {
            "Texto": (90, 650),
            "Imagen": (220, 1600),
            "Video": (320, 2100),
        },
        "tasa_interaccion": {
            "Texto": 0.085,
            "Imagen": 0.115,
            "Video": 0.130,
        },
    },
    "YouTube": {
        "tipo_alcance": "Visualizaciones",
        "tipo_interaccion": "Me gusta, comentarios y compartidos",
        "componentes": {
            "me_gusta": 0.58,
            "comentarios": 0.18,
            "compartidos": 0.14,
            "suscripciones": 0.10,
        },
        "alcance_por_formato": {
            "Texto": (80, 550),
            "Imagen": (140, 900),
            "Video": (520, 2800),
        },
        "tasa_interaccion": {
            "Texto": 0.045,
            "Imagen": 0.065,
            "Video": 0.095,
        },
    },
    "GitHub": {
        "tipo_alcance": "Vistas tecnicas",
        "tipo_interaccion": "Pushes, pull requests, issues y stars",
        "componentes": {
            "pushes": 0.44,
            "pull_requests": 0.18,
            "issues": 0.16,
            "stars": 0.22,
        },
        "alcance_por_formato": {
            "Texto": (60, 480),
            "Imagen": (80, 620),
            "Video": (120, 780),
        },
        "tasa_interaccion": {
            "Texto": 0.075,
            "Imagen": 0.085,
            "Video": 0.100,
        },
    },
}
