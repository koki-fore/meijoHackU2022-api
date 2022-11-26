from datetime import datetime
from pydantic import BaseModel

# from .user import User
# APIのリクエストやレスポンスの型を定義する

class Challenge_completedBase(BaseModel):
    challenge_FK: int
    user_FK: int

class Challenge_completedCreate(Challenge_completedBase):
    pass

class Challenge_completedCreateResponse(Challenge_completedBase):
    id: int
    created_at: datetime
    updated_at:datetime
    
    class Config:
        orm_mode = True
        
class Challenge_completed(Challenge_completedBase):
    id: int
    created_at: datetime
    updated_at:datetime
    
    # user: User
    
    class Config:
        orm_mode = True