from typing import Optional # Nullでも平気
from datetime import datetime
from pydantic import BaseModel, Field

# APIのリクエストやレスポンスの型を定義する

class Challenge_category(BaseModel):
    id: int
    challenge_FK: int
    category_FK: int
    created_at: datetime
    updated_at:datetime
    
    class Config:
        orm_mode = True