from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.db.models.file import StoredFile
from src.infrastructure.db.models.alert import Alert

class SqlAlchemyAlertRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def list_alerts(self, skip: int, max: int):
        result = await self.session.execute(
            select(Alert).offset(skip).limit(max).order_by(Alert.created_at.desc())
        )
        return result.scalars().all()

    async def create_alert(self, file_id: str, level: str, message: str):
        alert = Alert(file_id=file_id, level=level, message=message)
        self.session.add(alert)
        await self.session.commit()
        await self.session.refresh(alert)
        return alert
    