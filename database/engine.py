from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from database.config import db_settings


DATABASE_URL = db_settings.get_db_url()


engine = create_async_engine(url=DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
