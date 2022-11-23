from datetime import datetime
from pydantic import BaseModel, Field


# APIのリクエストやレスポンスの型を定義する

class CategoryBase(BaseModel):
    title: str = Field(None, example='地震')
    created_at: datetime
    updated_at: datetime
    
class CategoryCreate(CategoryBase):
    pass
    
class CategoryCreateResponse(CategoryBase):
    id: int

    class Config:
        orm_mode = True
    
class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True