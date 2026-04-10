from src.infrastructure.repositories.file_repo import SqlAlchemyFileRepository

class FilesDomainService:

    def __init__(self, repo: SqlAlchemyFileRepository):
        self.repo = repo

    async def list_files(self):
        return await self.repo.list_files()

    async def list_alerts(self):
        return await self.repo.list_alerts()

    async def get_file(self, file_id: str):
        file = await self.repo.get_file(file_id)
        if not file:
            raise ValueError("File not found")
        return file

    async def create_file(self, file):
        return await self.repo.create_file(file)

    async def update_file(self, file_id: str, title: str):
        return await self.repo.update_file(file_id, title)

    async def delete_file(self, file_id: str):
        return await self.repo.delete_file(file_id)

    async def create_alert(self, file_id: str, level: str, message: str):
        return await self.repo.create_alert(file_id, level, message)
    