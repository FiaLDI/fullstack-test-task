from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.db.models.file import StoredFile
from src.infrastructure.db.models.alert import Alert

class SqlAlchemyFileRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def list_files(self, skip: int, max: int):
        result = await self.session.execute(
            select(StoredFile).offset(skip).limit(max).order_by(StoredFile.created_at.desc())
        )
        return result.scalars().all()

    async def get_file(self, file_id: str):
        return await self.session.get(StoredFile, file_id)

    async def create_file(self, file: StoredFile):
        self.session.add(file)
        await self.session.commit()
        await self.session.refresh(file)
        return file

    async def update_file(self, file_id: str, title: str):
        file = await self.get_file(file_id)
        if not file:
            return None

        file.title = title
        await self.session.commit()
        await self.session.refresh(file)
        return file

    async def delete_file(self, file_id: str):
        file = await self.get_file(file_id)
        if not file:
            return

        await self.session.delete(file)
        await self.session.commit()
    