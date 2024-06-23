from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from data_models.base_model import DexBaseModel


class DexUser(DexBaseModel):
    __tablename__ = 'dex_user'
    __table_args__ = {'schema': 'public'} 
    
    telegram_id = Column(String, primary_key=True, index=True)
    wallet_address = Column(String, nullable=False)
    points = Column(Integer, nullable=True)
    referral_code = Column(String, nullable=False)
    claimed_code = Column(String, nullable=False)
    
    transactions = relationship("Transaction", back_populates="user")
    social_link = relationship("SocialLink", back_populates="user", uselist=False)
