from datetime import datetime
from pydantic import BaseModel

from .user import User
# APIのリクエストやレスポンスの型を定義する

class LikeBase(BaseModel):
    user_FK: int
    post_FK: int

class LikeCreate(LikeBase):
    pass

class LikeCreateResponse(LikeBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True
        
class Like(LikeBase):
    id: int
    created_at: datetime
    updated_at: datetime
    user: User
    
    class Config:
        orm_mode = True