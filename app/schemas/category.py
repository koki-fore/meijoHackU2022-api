from typing import Optional # Nullでも平気
from datetime import datetime
from pydantic import BaseModel, Field


# APIのリクエストやレスポンスの型を定義する

class CategoryBase(BaseModel):
    id: int
    title: str = Field(None, example='地震')
    created_at: datetime
    updated_at: datetime
    
class CategoryCreate(CategoryBase):
    pass