from datetime import datetime
from pydantic import BaseModel, validator
from typing import Optional, Union, List

class TransactionBase(BaseModel): 
    description:str
    date: datetime
    total:float 
    notes: Optional[str] = None 

    @validator('name')
    def name_len_checker(cls, name):
        if len(name) > 20:
            raise ValueError("Category name must not be longer than 20")
        return name
    
    @validator('total')
    def total_check(cls, total):
        if len(total) <= 0:
            raise ValueError("Total must be greater than 0")
        return total

class TransationGetRequest(BaseModel):
    page: Union[int, None] = None, 
    page_size: Union[int, None] = None,
    start_date: Union[datetime, None] = None, 
    end_date: Union[datetime, None] = None,  
    date_asc: bool = True,
    category_ids: Union[List[int], None] = None,

    # @validator('page')
    # def page_check(cls, page):
    #     if page < 0:
    #         raise ValueError("Page value can't be less than 0")
    #     return page
    
    # @validator('page_size')
    # def page_check(cls, page_size):
    #     if page_size <= 0 or page_size >= 200:
    #         raise ValueError("Page size can't be less than 1 or greater than 200")
    #     return page_size

class TransationsWithID():
    category_id: int

class TransactionCreate(TransationsWithID):
    pass

class TransactionUpdate(TransationsWithID):
    pass

