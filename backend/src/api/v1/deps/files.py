from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import async_session_maker
from src.infrastructure.repositories.file_repo import SqlAlchemyFileRepository
from src.domain.files.service import FilesDomainService


async def get_session():
    async with async_session_maker() as session:
        yield session


def get_file_service(
    session: AsyncSession = Depends(get_session),
) -> FilesDomainService:
    repo = SqlAlchemyFileRepository(session)
    return FilesDomainService(repo)
