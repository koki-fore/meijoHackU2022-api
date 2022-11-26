from datetime import datetime
from pydantic import BaseModel

# APIのリクエストやレスポンスの型を定義する

class Challenge_categoryBase(BaseModel):
    challenge_FK: int
    category_FK: int

class Challenge_categoryCreate(Challenge_categoryBase):
    pass

class Challenge_categoryCreateResponse(Challenge_categoryBase):
    id: int
    created_at: datetime
    updated_at:datetime
    
    class Config:
        orm_mode = True
        
class Challenge_category(Challenge_categoryBase):
    id: int
    created_at: datetime
    updated_at:datetime
    
    class Config:
        orm_mode = True