from __future__ import annotations

import base64
import hashlib
import hmac
import json
import secrets
import time

from models import Usuario
from repositories import PublicacionRepository, UsuarioRepository


class AuthService:
    DEFAULT_PASSWORD = "epis123"
    USERNAME_PREFIX = "2026"
    TOKEN_TTL_SECONDS = 60 * 60 * 8

    def __init__(
        self,
        publicacion_repository: PublicacionRepository,
        usuario_repository: UsuarioRepository,
        token_secret: str = "epis-dev-secret-change-me",
    ) -> None:
        self.publicacion_repository = publicacion_repository
        self.usuario_repository = usuario_repository
        self.token_secret = token_secret.encode("utf-8")

    def ensure_demo_users(self) -> None:
        self.usuario_repository.initialize_database()
        estudiantes = self.publicacion_repository.get_estudiantes()
        expected_usernames = [
            self._build_codigo_universitario(index)
            for index in range(1, len(estudiantes) + 1)
        ]

        if self.usuario_repository.count_users() > 0:
            current_usernames = self.usuario_repository.get_usernames()
            if current_usernames == expected_usernames:
                return

            self.usuario_repository.clear_all()

        usuarios = [
            Usuario(
                id=None,
                estudiante=estudiante,
                username=self._build_codigo_universitario(index),
                password_hash=self.hash_password(self.DEFAULT_PASSWORD),
            )
            for index, estudiante in enumerate(estudiantes, start=1)
        ]
        self.usuario_repository.save_many(usuarios)

    def login(self, username: str, password: str) -> dict[str, str | bool]:
        usuario = self.usuario_repository.find_by_username(username)

        if usuario is None or not self.verify_password(password, usuario.password_hash):
            return {
                "estudiante": username,
                "display_name": username,
                "username": username,
                "access_token": "",
                "token_type": "bearer",
                "is_authenticated": False,
            }

        return {
            "estudiante": usuario.estudiante,
            "display_name": usuario.estudiante,
            "username": usuario.username,
            "access_token": self.create_token(usuario),
            "token_type": "bearer",
            "is_authenticated": True,
        }

    def verify_token(self, token: str) -> dict[str, str]:
        try:
            payload_segment, signature_segment = token.split(".")
            expected_signature = self._sign(payload_segment)

            if not hmac.compare_digest(signature_segment, expected_signature):
                raise ValueError("Firma invalida.")

            payload = json.loads(self._base64url_decode(payload_segment))
            if int(payload["exp"]) < int(time.time()):
                raise ValueError("Token expirado.")

            return {
                "estudiante": str(payload["estudiante"]),
                "username": str(payload["username"]),
                "rol": str(payload["rol"]),
            }
        except Exception as error:
            raise ValueError("Token invalido.") from error

    def create_token(self, usuario: Usuario) -> str:
        payload = {
            "estudiante": usuario.estudiante,
            "username": usuario.username,
            "rol": usuario.rol,
            "exp": int(time.time()) + self.TOKEN_TTL_SECONDS,
        }
        payload_segment = self._base64url_encode(json.dumps(payload).encode("utf-8"))
        signature_segment = self._sign(payload_segment)
        return f"{payload_segment}.{signature_segment}"

    def hash_password(self, password: str) -> str:
        salt = secrets.token_hex(16)
        password_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt.encode("utf-8"),
            120_000,
        ).hex()
        return f"{salt}${password_hash}"

    def verify_password(self, password: str, stored_hash: str) -> bool:
        salt, password_hash = stored_hash.split("$", maxsplit=1)
        candidate_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt.encode("utf-8"),
            120_000,
        ).hex()
        return hmac.compare_digest(candidate_hash, password_hash)

    def _build_codigo_universitario(self, index: int) -> str:
        return f"{self.USERNAME_PREFIX}{index:04d}"

    def _sign(self, payload_segment: str) -> str:
        signature = hmac.new(
            self.token_secret,
            payload_segment.encode("utf-8"),
            hashlib.sha256,
        ).digest()
        return self._base64url_encode(signature)

    def _base64url_encode(self, data: bytes) -> str:
        return base64.urlsafe_b64encode(data).decode("utf-8").rstrip("=")

    def _base64url_decode(self, data: str) -> bytes:
        padding = "=" * (-len(data) % 4)
        return base64.urlsafe_b64decode(data + padding)
