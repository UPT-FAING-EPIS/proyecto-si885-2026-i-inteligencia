from functools import lru_cache

import pandas as pd
from fastapi import Depends, HTTPException, Request, status

from models import REDES_SOCIALES, TODAS_LAS_REDES
from repositories import SQLitePublicacionRepository, SQLiteUsuarioRepository
from services import AnalyticsService, AuthService, GeneradorDatosService


DB_PATH = "epis_data.db"


@lru_cache(maxsize=1)
def get_repository() -> SQLitePublicacionRepository:
    return SQLitePublicacionRepository.get_instance(DB_PATH)


@lru_cache(maxsize=1)
def get_usuario_repository() -> SQLiteUsuarioRepository:
    return SQLiteUsuarioRepository.get_instance(DB_PATH)


def get_data_service() -> GeneradorDatosService:
    return GeneradorDatosService(repository=get_repository())


def get_analytics_service() -> AnalyticsService:
    return AnalyticsService(repository=get_repository())


def get_auth_service() -> AuthService:
    return AuthService(
        publicacion_repository=get_repository(),
        usuario_repository=get_usuario_repository(),
    )


def require_authenticated_session(
    request: Request,
    auth_service: AuthService = Depends(get_auth_service),
) -> dict[str, str]:
    authorization = request.headers.get("Authorization", "")

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de autenticacion requerido.",
        )

    token = authorization.removeprefix("Bearer ").strip()

    try:
        return auth_service.verify_token(token)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(error),
        ) from error


def normalize_red_social(red_social: str | None) -> str | None:
    if not red_social or red_social == TODAS_LAS_REDES:
        return None

    if red_social not in REDES_SOCIALES:
        raise ValueError(f"Red social no valida: {red_social}")

    return red_social


def dataframe_to_records(data: pd.DataFrame) -> list[dict]:
    if data.empty:
        return []

    records = data.copy()

    for column in records.columns:
        if pd.api.types.is_datetime64_any_dtype(records[column]):
            records[column] = records[column].dt.strftime("%Y-%m-%d")
        elif isinstance(records[column].dtype, pd.CategoricalDtype):
            records[column] = records[column].astype(str)

    return records.to_dict(orient="records")
