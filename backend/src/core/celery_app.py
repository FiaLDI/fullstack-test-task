
from celery import Celery
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.core.config import REDIS_URL, DB_URL

celery_app = Celery("file_tasks", broker=REDIS_URL, backend=REDIS_URL)
engine = create_async_engine(DB_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
