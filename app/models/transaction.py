from datetime import datetime
from pydantic import BaseModel, Field, validator
from typing import Optional

class Transaction(BaseModel):
    id:int  = Field(default=None, primary_key=True)
    description:str
    date: datetime
    total:float 
    notes: Optional[str] = None
    category_id: int 

    class Config:
        orm_mode = True

