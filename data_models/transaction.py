from base_model import *


class Transaction(DexBaseModel):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(String, ForeignKey('dex_user.telegram_id'), nullable=False)
    market = Column(String, nullable=False)
    type = Column(String, nullable=False)
    side = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)
    
    user = relationship("User", back_populates="transactions")