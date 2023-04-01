from pydantic import BaseModel
from datetime import datetime

class ItemBase(BaseModel):
    title: str

class ItemDisplay(BaseModel):
    id: int
    title: str
    timestamp: datetime
    class Config():
        orm_load = True