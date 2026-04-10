import asyncio
from pathlib import Path

from src.core.database import async_session_maker
from src.infrastructure.repositories.file_repo import SqlAlchemyFileRepository
from src.domain.files.service import FilesDomainService
from src.domain.files.handlers import FileProcessingHandler, MetadataHandler
from src.core.celery_app import celery_app

STORAGE_DIR = Path("storage")


def run_async(coro):
    return asyncio.run(coro)


@celery_app.task
def scan_file_for_threats(file_id: str):
    async def task():
        async with async_session_maker() as session:
            repo = SqlAlchemyFileRepository(session)
            service = FilesDomainService(repo)
            handler = FileProcessingHandler(service)

            await handler.scan_file(file_id)

    run_async(task())

    extract_file_metadata.delay(file_id)


@celery_app.task
def extract_file_metadata(file_id: str):
    async def task():
        async with async_session_maker() as session:
            repo = SqlAlchemyFileRepository(session)
            service = FilesDomainService(repo)
            handler = MetadataHandler(service)

            await handler.extract_metadata(file_id, STORAGE_DIR)

    run_async(task())

    send_file_alert.delay(file_id)


@celery_app.task
def send_file_alert(file_id: str):
    async def task():
        async with async_session_maker() as session:
            repo = SqlAlchemyFileRepository(session)
            service = FilesDomainService(repo)

            file = await service.get_file(file_id)

            if file.requires_attention:
                await service.create_alert(
                    file.id,
                    "warning",
                    file.scan_details,
                )
            else:
                await service.create_alert(
                    file.id,
                    "info",
                    "File processed successfully",
                )

    run_async(task())
