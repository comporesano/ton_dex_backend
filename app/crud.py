from fastapi import HTTPException
from sqlalchemy.future import select
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from data_models import transaction, dex_user, social_links
from refferal_code_generator import CodeGenerator
from typing import Coroutine



class DexCrud:
    
    
    @staticmethod
    async def get_user_by_referral_code(db: AsyncSession, referral_code: str) -> Coroutine:
        result = await db.execute(select(dex_user.DexUser).filter(dex_user.DexUser.referral_code == referral_code))
        return result.scalars().first()
    
    @staticmethod
    async def get_user(database: AsyncSession, tg_id: str) -> Coroutine:
        result = await database.execute(select(dex_user.DexUser).filter(dex_user.DexUser.telegram_id == tg_id))
        return result
    
    @staticmethod
    async def create_user(database: AsyncSession, telegram_id: str, wallet_address: str = '', claimed_code: str = '') -> dex_user.DexUser:
        code = CodeGenerator().code
        existing_user = await DexCrud.get_user_by_referral_code(database, code)
        while existing_user:
            code = CodeGenerator().code
            existing_user = await DexCrud.get_user_by_referral_code(database, code)
        db_user = dex_user.DexUser(
            telegram_id=telegram_id,
            wallet_address=wallet_address,
            points=0,
            referral_code=code,
            claimed_code=claimed_code
        )
        database.add(db_user)
        await database.commit()
        await database.refresh(db_user)
        return db_user
        
    @staticmethod
    async def append_transaction(database: AsyncSession, telegram_id: str, market: str, type: str, side: str, amount: int, price: float, timestamp: TIMESTAMP) -> transaction.Transaction:
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
    
    async def get_user_with_details(db: AsyncSession, telegram_id: str):
        result = await db.execute(select(dex_user.DexUser).filter(dex_user.DexUser.telegram_id == telegram_id).options(selectinload(dex_user.DexUser.transactions), selectinload(dex_user.DexUser.social_link)))
        return result.scalars().first()

    @staticmethod
    async def set_social_link(database: AsyncSession, telegram_id: str, social_link_type: str, link: str) -> social_links.SocialLink:
        result = await database.execute(select(social_link.SocialLink).filter(social_link.SocialLink.telegram_id == telegram_id))
        social_link = result.scalars().first()

        if social_link is None:
            raise HTTPException(status_code=404, detail="Social link not found for the user")

        if social_link_type == 'site':
            social_link.site_link = link
        elif social_link_type == 'twitter':
            social_link.twitter_link = link
        elif social_link_type == 'telegram':
            social_link.telegram_link = link
        elif social_link_type == 'discord':
            social_link.discord_link = link
        else:
            raise HTTPException(status_code=400, detail="Invalid social link type")

        database.add(social_link)
        await database.commit()
        await database.refresh(social_link)
        return social_link