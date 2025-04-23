from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from database.db_models import Base

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3', echo = True)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)