from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.data_models.base_model import DexBaseModel


class Transaction(DexBaseModel):
    __tablename__ = "transactions"
    __table_args__ = {'schema': 'public'} 

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(String, ForeignKey('public.dex_user.telegram_id'), nullable=False)
    market = Column(String, nullable=False)
    type = Column(String, nullable=False)
    side = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)
    
    user = relationship("DexUser", back_populates="transactions")
