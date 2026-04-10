import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.infrastructure.db.base import Base
from src.infrastructure.db.models.file import StoredFile
from src.infrastructure.repositories.file_repo import SqlAlchemyFileRepository
from src.domain.files.service import FilesDomainService

TEST_DB = "sqlite+aiosqlite:///:memory:"


async def get_session():
    engine = create_async_engine(TEST_DB)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    session_maker = async_sessionmaker(engine, expire_on_commit=False)

    async with session_maker() as session:
        yield session


async def test_service_create_get():
    async for session in get_session():
        repo = SqlAlchemyFileRepository(session)
        service = FilesDomainService(repo)

        file = StoredFile(
            id="1",
            title="Test",
            original_name="file.txt",
            stored_name="file.txt",
            mime_type="text/plain",
            size=10,
            processing_status="uploaded",
        )

        await service.create_file(file)

        result = await service.get_file("1")

        assert result.id == "1"
        assert result.title == "Test"
        