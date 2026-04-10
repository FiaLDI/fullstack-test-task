from fastapi import APIRouter, Depends
from pathlib import Path

from src.api.v1.deps.files import get_file_service
from src.domain.files.service import FilesDomainService
from src.schemas import AlertItem

router = APIRouter()


@router.get("/", response_model=list[AlertItem])
async def list_alerts(service: FilesDomainService = Depends(get_file_service)):
    return await service.list_alerts()

