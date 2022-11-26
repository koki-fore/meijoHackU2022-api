from datetime import datetime
from pydantic import BaseModel, Field


# APIのリクエストやレスポンスの型を定義する

class CategoryBase(BaseModel):
    title: str = Field(None, example='地震')
    
class CategoryCreate(CategoryBase):
    pass
    
class CategoryCreateResponse(CategoryBase):
    id: int
    created_at: datetime
    updated_at:datetime

    class Config:
        orm_mode = True
    
class Category(CategoryBase):
    id: int
    created_at: datetime
    updated_at:datetime

    class Config:
        orm_mode = True