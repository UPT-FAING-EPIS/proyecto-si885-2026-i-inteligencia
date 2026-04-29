from controllers import AppController
from repositories import SQLitePublicacionRepository
from services import AnalyticsService, GeneradorDatosService
from views import StreamlitDashboardView


DB_PATH = "epis_data.db"


def build_app() -> AppController:
    repository = SQLitePublicacionRepository.get_instance(DB_PATH)
    data_service = GeneradorDatosService(repository=repository)
    analytics_service = AnalyticsService(repository=repository)
    view = StreamlitDashboardView()
    view.configure_page()

    return AppController(
        repository=repository,
        data_service=data_service,
        analytics_service=analytics_service,
        view=view,
    )


def main() -> None:
    app = build_app()
    app.run()


if __name__ == "__main__":
    main()
