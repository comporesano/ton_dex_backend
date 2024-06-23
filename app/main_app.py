from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse
from database.database import DexDatabase
from data_models import base_model
import crud

db = DexDatabase()

async def lifespan(app: FastAPI):
    async with db.engine.begin() as conn:
        await conn.run_sync(base_model.DexBaseModel.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = JSONResponse({"detail": "Internal server error"}, status_code=500)
    try:
        async for session in db.get_async_session():
            request.state.db = session
            response = await call_next(request)
    finally:
        if hasattr(request.state, 'db'):
            await request.state.db.close()
    return response

def get_db(request: Request):
    return request.state.db

@app.post("/user/")
async def create_user(db: AsyncSession = Depends(get_db), telegram_id: str = '', wallet_address: str = '', claimed_code: str = ''):
    return await crud.DexCrud.create_user(db, telegram_id, wallet_address, claimed_code)

@app.get("/user/{telegram_id}")
async def read_user(telegram_id: str, db: AsyncSession = Depends(get_db)):
    db_user = await crud.DexCrud.get_user_with_details(db, telegram_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/transaction/")
async def create_transaction(telegram_id: str, market: str, type: str, side: str, amount: int, price: float, timestamp: str, db: AsyncSession = Depends(get_db)):
    return await crud.DexCrud.create_transaction(db, telegram_id, market, type, side, amount, price, timestamp)

@app.put("/sociallink/{telegram_id}")
async def update_social_link(telegram_id: str, social_link_type: str, link: str, db: AsyncSession = Depends(get_db)):
    return await crud.DexCrud.set_social_link(db, telegram_id, social_link_type, link)
