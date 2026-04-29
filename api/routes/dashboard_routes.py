from fastapi import APIRouter, Depends, HTTPException, Query, status

from api.dependencies import dataframe_to_records, normalize_red_social
from api.schemas import GlobalResponse, PerfilResponse
from repositories import PublicacionRepository
from services import AnalyticsService

from ..dependencies import (
    get_analytics_service,
    get_repository,
    require_authenticated_session,
)


router = APIRouter(prefix="/api", tags=["dashboard"])


@router.get("/estudiantes", response_model=list[str])
def get_estudiantes(
    repository: PublicacionRepository = Depends(get_repository),
) -> list[str]:
    return repository.get_estudiantes()


@router.get("/dashboard/perfil", response_model=PerfilResponse)
def get_perfil(
    estudiante: str = Query(..., min_length=1),
    red_social: str | None = None,
    session: dict[str, str] = Depends(require_authenticated_session),
    repository: PublicacionRepository = Depends(get_repository),
    analytics_service: AnalyticsService = Depends(get_analytics_service),
) -> PerfilResponse:
    if estudiante not in repository.get_estudiantes():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Estudiante no encontrado.",
        )

    try:
        normalized_red = normalize_red_social(red_social)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error

    return PerfilResponse(
        metricas=analytics_service.get_metricas_estudiante(
            estudiante,
            red_social=normalized_red,
        ),
        interacciones_tiempo=dataframe_to_records(
            analytics_service.get_interacciones_tiempo(
                estudiante,
                red_social=normalized_red,
            )
        ),
        interacciones_por_red=dataframe_to_records(
            analytics_service.get_interacciones_por_red(
                estudiante=estudiante,
                red_social=normalized_red,
            )
        ),
        detalle_interacciones=dataframe_to_records(
            analytics_service.get_detalle_interacciones(
                estudiante=estudiante,
                red_social=normalized_red,
            )
        ),
        contexto_red=analytics_service.get_contexto_red(red_social=normalized_red),
    )


@router.get("/dashboard/global", response_model=GlobalResponse)
def get_global(
    red_social: str | None = None,
    session: dict[str, str] = Depends(require_authenticated_session),
    analytics_service: AnalyticsService = Depends(get_analytics_service),
) -> GlobalResponse:
    try:
        normalized_red = normalize_red_social(red_social)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error

    return GlobalResponse(
        alcance_por_ciclo=dataframe_to_records(
            analytics_service.get_alcance_por_ciclo(red_social=normalized_red)
        ),
        interacciones_por_red=dataframe_to_records(
            analytics_service.get_interacciones_por_red(red_social=normalized_red)
        ),
        detalle_interacciones=dataframe_to_records(
            analytics_service.get_detalle_interacciones(red_social=normalized_red)
        ),
        top_engagement=dataframe_to_records(
            analytics_service.get_top_engagement(
                limit=10,
                red_social=normalized_red,
            )
        ),
        contexto_red=analytics_service.get_contexto_red(red_social=normalized_red),
    )
