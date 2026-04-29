from fastapi import APIRouter, Depends, HTTPException, status

from api.schemas import LoginRequest, SessionResponse
from services import AuthService

from ..dependencies import get_auth_service, require_authenticated_session


router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/login", response_model=SessionResponse)
def login(
    request: LoginRequest,
    auth_service: AuthService = Depends(get_auth_service),
) -> SessionResponse:
    session = auth_service.login(request.username, request.password)

    if not session["is_authenticated"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales invalidas.",
        )

    return SessionResponse(**session)


@router.get("/me")
def me(
    session: dict[str, str] = Depends(require_authenticated_session),
) -> dict[str, str]:
    return session


@router.post("/logout")
def logout() -> dict[str, bool]:
    return {"ok": True}
