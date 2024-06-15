from base_model import *


class SocialLink(DexBaseModel):
    __tablename__ = "social_links"

    telegram_id = Column(String, ForeignKey('dex_user.telegram_id'), nullable=False)
    site_link = Column(String, nullable=True)
    twitter_link = Column(String, nullable=True)
    telegram_link = Column(String, nullable=True)
    discord_link = Column(String, nullable=True)