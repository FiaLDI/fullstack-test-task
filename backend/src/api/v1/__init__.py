from fastapi import APIRouter
from src.api.v1.endpoints.files import router as files_router
from src.api.v1.endpoints.alert import router as alert_router


api_router = APIRouter()
api_router.include_router(files_router, prefix="/files", tags=["files"])
api_router.include_router(alert_router, prefix="/alerts", tags=["alert"])
