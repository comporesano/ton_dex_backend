from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from data_models import transaction, dex_user, social_links
from typing import Coroutine
from refferal_code_generator import CodeGenerator


class DexCrud:
    
    
    @staticmethod
    async def get_user(database: AsyncSession, tg_id: str) -> Coroutine:
        result = await database.execute(select(dex_user.DexUser).filter(dex_user.DexUser.telegram_id == tg_id))
        return result
    
    @staticmethod
    async def create_user(database: AsyncSession, telegram_id: str, wallet_address: str = '', claimed_code: str = ''):
        db_user = dex_user.User(
            telegram_id=telegram_id,
            wallet_address=wallet_address,
            points=0,
            referral_code=CodeGenerator().code,
            claimed_code=claimed_code
        )
        database.add(db_user)
        await database.commit()
        await database.refresh(db_user)
        return db_user
    
    @staticmethod
    async def append_transaction(database: AsyncSession, telegram_id: str, market: str, type: str, side: str, amount: int, price: float, timestamp: TIMESTAMP):
        db_transaction = transaction.Transaction(
            telegram_id=telegram_id,
            market=market,
            type=type,
            side=side,
            amount=amount,
            price=price,
            timestamp=timestamp
        )
        database.add(db_transaction)
        await database.commit()
        await database.refresh(db_transaction)
        return db_transaction