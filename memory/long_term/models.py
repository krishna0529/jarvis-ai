# pyrefly: ignore [missing-import]
from sqlalchemy.orm import DeclarativeBase
# pyrefly: ignore [missing-import]
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
    pass


class UserMemory(Base):

    __tablename__ = "user_memory"

    id = Column(Integer, primary_key=True)

    key = Column(String)

    value = Column(String)
