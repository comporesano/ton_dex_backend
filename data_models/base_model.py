from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, ForeignKey


class DexBaseModel(DeclarativeBase):
    pass