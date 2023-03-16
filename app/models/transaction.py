from datetime import datetime
from pydantic import BaseModel, validator
from typing import Optional, Union, List
from fastapi import Body

class TransactionBase(BaseModel): 
    description:str
    date: datetime
    total:float 
    notes: Optional[str] = None 
    category_id: int 

    @validator('description')
    def description_check(cls, description):
        if len(description) > 40:
            raise ValueError("Transactiion description can't exceed 50")
        return description
    
    @validator('total')
    def total_check(cls, total):
        if total <= 0:
            raise ValueError("Total must be greater than 0")
        return total
    
    @validator('notes')
    def notes_check(cls, notes):
        if len(notes) > 200:
            raise ValueError("Notes must not exceed 200 character")
        return notes

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(TransactionBase):
    pass

class TransationsRequest(BaseModel):
    page: Optional[int] = 1
    page_size: Optional[int] = 30
    start_date: Optional[datetime] = datetime(2010, 2, 15, 18, 54, 58, 291224)
    end_date: Optional[datetime] = datetime.now() 
    date_asc: bool = True
    category_ids: Optional[List[int]] = []


    # @validator('page', 'page_size', 'start_date', 'end_date', 'category_ids', pre=True)
    # def allow_none(cls, v):
    #     if v is None:
    #          return None
    #     else:
    #         return v
    

