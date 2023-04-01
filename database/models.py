from .database import Base
from sqlalchemy import Column, String, Integer, DateTime

class DbItem(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    timestamp = Column(DateTime)

