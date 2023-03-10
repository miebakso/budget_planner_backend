from pydantic import BaseModel, Field
from typing import Optional

class Category(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    name:str 

