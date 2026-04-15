from fastapi import APIRouter, Depends, Query
from pathlib import Path

from src.api.v1.deps.alert import get_alert_service
from src.domain.alert.service import AlertsDomainService
from src.infrastructure.db.schemas import AlertItem

router = APIRouter()


@router.get("/", response_model=list[AlertItem])
async def list_alerts(
    skip: int = Query(0, ge=0),
    max: int = Query(10, ge=1, le=100),
    service: AlertsDomainService = Depends(get_alert_service)):
    return await service.list_alerts(skip=skip, max=max)
