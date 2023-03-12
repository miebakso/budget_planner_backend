from pydantic import BaseModel, Field, validator
from typing import Optional

class BaseCategory(BaseModel):
    name:str 

    @validator('name')
    def name_len_checker(cls, name):
        if len(name) > 20:
            raise ValueError("Category name must not be longer than 20")
        return name

class Category(BaseCategory):
    id: int 

class CategoryCreate(BaseCategory):
    pass

class CategoryUpdate(BaseCategory):
    pass



