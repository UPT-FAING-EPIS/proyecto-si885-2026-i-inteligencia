from typing import Any

from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class SessionResponse(BaseModel):
    estudiante: str
    display_name: str
    username: str
    access_token: str
    token_type: str
    is_authenticated: bool


class PerfilResponse(BaseModel):
    metricas: dict[str, int | str]
    interacciones_tiempo: list[dict[str, Any]]
    interacciones_por_red: list[dict[str, Any]]
    detalle_interacciones: list[dict[str, Any]]
    contexto_red: dict[str, Any]


class GlobalResponse(BaseModel):
    alcance_por_ciclo: list[dict[str, Any]]
    interacciones_por_red: list[dict[str, Any]]
    detalle_interacciones: list[dict[str, Any]]
    top_engagement: list[dict[str, Any]]
    contexto_red: dict[str, Any]
