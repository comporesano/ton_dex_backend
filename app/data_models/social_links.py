from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from data_models.base_model import DexBaseModel


class SocialLink(DexBaseModel):
    __tablename__ = "social_links"
    __table_args__ = {'schema': 'public'} 

    telegram_id = Column(String, ForeignKey('public.dex_user.telegram_id'), primary_key=True, nullable=False)
    site_link = Column(String, nullable=True)
    twitter_link = Column(String, nullable=True)
    telegram_link = Column(String, nullable=True)
    discord_link = Column(String, nullable=True)
    
    user = relationship("DexUser", back_populates="social_link")