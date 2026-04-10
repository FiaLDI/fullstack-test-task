from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
from uuid import uuid4
import mimetypes

from src.api.v1.deps.files import get_file_service
from src.domain.files.service import FilesDomainService
from src.infrastructure.db.models.file import StoredFile
from src.schemas import FileItem, AlertItem, FileUpdate
from src.infrastructure.tasks.file_tasks import scan_file_for_threats

router = APIRouter()

STORAGE_DIR = Path("storage")
STORAGE_DIR.mkdir(exist_ok=True)


@router.get("/", response_model=list[FileItem])
async def list_files(service: FilesDomainService = Depends(get_file_service)):
    return await service.list_files()

@router.post("/", response_model=FileItem, status_code=201)
async def create_file(
    title: str = Form(...),
    file: UploadFile = File(...),
    service: FilesDomainService = Depends(get_file_service),
):
    content = await file.read()
    if not content:
        raise HTTPException(400, "Empty file")

    file_id = str(uuid4())
    suffix = Path(file.filename or "").suffix
    stored_name = f"{file_id}{suffix}"

    path = STORAGE_DIR / stored_name
    path.write_bytes(content)

    db_file = StoredFile(
        id=file_id,
        title=title,
        original_name=file.filename or stored_name,
        stored_name=stored_name,
        mime_type=file.content_type or mimetypes.guess_type(stored_name)[0] or "application/octet-stream",
        size=len(content),
        processing_status="uploaded",
    )

    saved = await service.create_file(db_file)

    scan_file_for_threats.delay(saved.id)

    return saved


@router.get("/{file_id}", response_model=FileItem)
async def get_file(
    file_id: str,
    service: FilesDomainService = Depends(get_file_service),
):
    file = await service.get_file(file_id)
    if not file:
        raise HTTPException(404, "File not found")
    return file


@router.patch("/{file_id}", response_model=FileItem)
async def update_file(
    file_id: str,
    payload: FileUpdate,
    service: FilesDomainService = Depends(get_file_service),
):
    file = await service.update_file(file_id, payload.title)
    if not file:
        raise HTTPException(404, "File not found")
    return file


@router.get("/{file_id}/download")
async def download_file(
    file_id: str,
    service: FilesDomainService = Depends(get_file_service),
):
    file = await service.get_file(file_id)
    if not file:
        raise HTTPException(404, "File not found")

    path = STORAGE_DIR / file.stored_name
    if not path.exists():
        raise HTTPException(404, "Stored file not found")

    return FileResponse(
        path=path,
        media_type=file.mime_type,
        filename=file.original_name,
    )


@router.delete("/{file_id}", status_code=204)
async def delete_file(
    file_id: str,
    service: FilesDomainService = Depends(get_file_service),
):
    await service.delete_file(file_id)
