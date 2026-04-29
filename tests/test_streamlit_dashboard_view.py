import pandas as pd

from controllers.navigation import GLOBAL_VIEW, PERFIL_VIEW
from models import TODAS_LAS_REDES
from views import StreamlitDashboardView


class FakeFigure:
    def __init__(self) -> None:
        self.traces = []
        self.layout = {}

    def update_traces(self, **kwargs) -> None:
        self.traces.append(kwargs)

    def update_layout(self, **kwargs) -> None:
        self.layout.update(kwargs)


class FakePlotlyExpress:
    def __init__(self) -> None:
        self.line_args = None
        self.bar_args = None
        self.figure = FakeFigure()

    def line(self, *args, **kwargs) -> FakeFigure:
        self.line_args = {"args": args, "kwargs": kwargs}
        return self.figure

    def bar(self, *args, **kwargs) -> FakeFigure:
        self.bar_args = {"args": args, "kwargs": kwargs}
        return self.figure


class FakeSidebar:
    def __init__(
        self,
        selected_view: str = PERFIL_VIEW,
        selected_red: str = TODAS_LAS_REDES,
    ) -> None:
        self.selected_view = selected_view
        self.selected_red = selected_red
        self.titles = []
        self.radio_args = None
        self.selectbox_args = []
        self.messages = []

    def title(self, text: str) -> None:
        self.titles.append(text)

    def radio(self, label: str, options) -> str:
        self.radio_args = (label, options)
        return self.selected_view

    def selectbox(self, label: str, options: list[str]) -> str:
        self.selectbox_args.append((label, options))
        if label == "Red social":
            return self.selected_red
        return options[0]

    def info(self, message: str) -> None:
        self.messages.append(message)


class FakeColumn:
    def __init__(self) -> None:
        self.metrics = []

    def metric(self, label: str, value) -> None:
        self.metrics.append((label, value))


class FakeStreamlit:
    def __init__(
        self,
        selected_view: str = PERFIL_VIEW,
        selected_red: str = TODAS_LAS_REDES,
    ) -> None:
        self.sidebar = FakeSidebar(selected_view, selected_red)
        self.page_config = None
        self.headers = []
        self.subheaders = []
        self.messages = []
        self.columns_created = []
        self.charts = []
        self.dataframes = []

    def set_page_config(self, **kwargs) -> None:
        self.page_config = kwargs

    def header(self, text: str) -> None:
        self.headers.append(text)

    def subheader(self, text: str) -> None:
        self.subheaders.append(text)

    def info(self, message: str) -> None:
        self.messages.append(message)

    def columns(self, count: int) -> list[FakeColumn]:
        columns = [FakeColumn() for _ in range(count)]
        self.columns_created.append(columns)
        return columns

    def plotly_chart(self, figure: FakeFigure, use_container_width: bool) -> None:
        self.charts.append((figure, use_container_width))

    def dataframe(self, data: pd.DataFrame, use_container_width: bool, hide_index: bool):
        self.dataframes.append((data, use_container_width, hide_index))


def test_configure_page_define_layout_ancho() -> None:
    st = FakeStreamlit()
    view = StreamlitDashboardView(st_module=st, px_module=FakePlotlyExpress())

    view.configure_page()

    assert st.page_config == {
        "page_title": "EPIS Analytics",
        "page_icon": ":bar_chart:",
        "layout": "wide",
    }


def test_render_sidebar_retorna_vista_y_estudiante() -> None:
    st = FakeStreamlit(selected_view=PERFIL_VIEW)
    view = StreamlitDashboardView(st_module=st, px_module=FakePlotlyExpress())

    view_name, estudiante, red_social = view.render_sidebar(["Ana Perez", "Luis Rojas"])

    assert view_name == PERFIL_VIEW
    assert estudiante == "Ana Perez"
    assert red_social is None
    assert st.sidebar.selectbox_args == [
        ("Red social", ["Todas", "LinkedIn", "Instagram", "YouTube", "GitHub"]),
        ("Estudiante", ["Ana Perez", "Luis Rojas"]),
    ]


def test_render_sidebar_retorna_red_social_filtrada() -> None:
    st = FakeStreamlit(selected_view=PERFIL_VIEW, selected_red="YouTube")
    view = StreamlitDashboardView(st_module=st, px_module=FakePlotlyExpress())

    _, _, red_social = view.render_sidebar(["Ana Perez"])

    assert red_social == "YouTube"


def test_render_sidebar_global_no_pide_estudiante() -> None:
    st = FakeStreamlit(selected_view=GLOBAL_VIEW)
    view = StreamlitDashboardView(st_module=st, px_module=FakePlotlyExpress())

    view_name, estudiante, red_social = view.render_sidebar(["Ana Perez"])

    assert view_name == GLOBAL_VIEW
    assert estudiante is None
    assert red_social is None
    assert st.sidebar.selectbox_args == [
        ("Red social", ["Todas", "LinkedIn", "Instagram", "YouTube", "GitHub"])
    ]


def test_render_metricas_dibuja_tres_metricas() -> None:
    st = FakeStreamlit()
    view = StreamlitDashboardView(st_module=st, px_module=FakePlotlyExpress())

    view.render_metricas(
        {
            "total_publicaciones": 5,
            "total_interacciones": 250,
            "red_favorita": "LinkedIn",
        }
    )

    metrics = [column.metrics[0] for column in st.columns_created[0]]
    assert metrics == [
        ("Publicaciones", 5),
        ("Interacciones", 250),
        ("Red favorita", "LinkedIn"),
    ]


def test_render_line_chart_con_datos_usa_plotly() -> None:
    st = FakeStreamlit()
    px = FakePlotlyExpress()
    view = StreamlitDashboardView(st_module=st, px_module=px)
    data = pd.DataFrame(
        {
            "fecha": pd.to_datetime(["2026-01-01"]),
            "interacciones": [120],
        }
    )

    view.render_line_chart(data)

    assert px.line_args["kwargs"]["x"] == "fecha"
    assert px.line_args["kwargs"]["y"] == "interacciones"
    assert st.charts == [(px.figure, True)]


def test_render_bar_chart_con_datos_usa_plotly() -> None:
    st = FakeStreamlit()
    px = FakePlotlyExpress()
    view = StreamlitDashboardView(st_module=st, px_module=px)
    data = pd.DataFrame({"ciclo": ["VII"], "alcance": [1000]})

    view.render_bar_chart(data)

    assert px.bar_args["kwargs"]["x"] == "ciclo"
    assert px.bar_args["kwargs"]["y"] == "alcance"
    assert st.charts == [(px.figure, True)]


def test_render_interacciones_red_chart_con_datos_usa_plotly() -> None:
    st = FakeStreamlit()
    px = FakePlotlyExpress()
    view = StreamlitDashboardView(st_module=st, px_module=px)
    data = pd.DataFrame({"red_social": ["LinkedIn"], "interacciones": [250]})

    view.render_interacciones_red_chart(data)

    assert px.bar_args["kwargs"]["x"] == "red_social"
    assert px.bar_args["kwargs"]["y"] == "interacciones"
    assert st.charts == [(px.figure, True)]


def test_render_top_table_formatea_engagement() -> None:
    st = FakeStreamlit()
    view = StreamlitDashboardView(st_module=st, px_module=FakePlotlyExpress())
    data = pd.DataFrame(
        {
            "estudiante": ["Ana Perez"],
            "publicaciones": [3],
            "alcance": [100],
            "interacciones": [25],
            "engagement_rate": [0.25],
        }
    )

    view.render_top_table(data)

    rendered, use_container_width, hide_index = st.dataframes[0]
    assert use_container_width is True
    assert hide_index is True
    assert rendered.columns.tolist() == [
        "Estudiante",
        "Publicaciones",
        "Alcance",
        "Interacciones",
        "Engagement (%)",
    ]
    assert rendered.loc[0, "Engagement (%)"] == 25.0
