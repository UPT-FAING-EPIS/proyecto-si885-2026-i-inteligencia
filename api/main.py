from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.dependencies import get_auth_service, get_data_service
from api.routes import auth_router, dashboard_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    data_service = get_data_service()
    data_service.ensure_seed_data()
    auth_service = get_auth_service()
    auth_service.ensure_demo_users()
    yield


app = FastAPI(
    title="EPIS Analytics API",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "http://127.0.0.1:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(dashboard_router)


@app.get("/api/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
