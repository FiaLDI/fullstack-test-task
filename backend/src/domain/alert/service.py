from src.infrastructure.repositories.alert_repo import SqlAlchemyAlertRepository

class AlertsDomainService:

    def __init__(self, repo: SqlAlchemyAlertRepository):
        self.repo = repo

    async def list_alerts(self, skip: int, max: int):
        return await self.repo.list_alerts(skip=skip, max=max)

    async def create_alert(self, file_id: str, level: str, message: str):
        return await self.repo.create_alert(file_id, level, message)
    