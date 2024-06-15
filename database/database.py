from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator
from settings import DB_PASSW


class DexDatabase:
    
    
    def __init__(self) -> None:
        self.database_url = f"postgresql+asyncpg://obelisk_dex_admin:{DB_PASSW}@localhost/ton_dex"
        self.engine = create_async_engine(self.database_url, echo=True)
        self.async_session = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )
    
    async def get_data_base(self) -> AsyncGenerator:
        async with self.async_session() as session:
            yield session
            await session.commit()