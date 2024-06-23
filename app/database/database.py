from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from typing import AsyncGenerator


class DexDatabase:
    def __init__(self):
        self.database_url = "postgresql+asyncpg://obelisk_dex_admin:hmtmUh8r0tJheehpqu1L@db:5432/ton_dex"
        self.engine = create_async_engine(self.database_url, echo=True)
        self.async_session = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )
        self.sync_engine = create_engine(self.database_url)

    async def get_async_session(self) -> AsyncGenerator:
        async with self.async_session() as session:
            yield session
            await session.commit()

    def get_sync_session(self):
        return self.sync_engine.connect()
