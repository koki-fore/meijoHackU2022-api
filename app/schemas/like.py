from datetime import datetime
from pydantic import BaseModel

# APIのリクエストやレスポンスの型を定義する

class LikeBase(BaseModel):
    user_FK: int
    post_FK: int
    created_at: datetime
    updated_at: datetime

class LikeCreate(LikeBase):
    pass

class LikeCreateResponse(LikeBase):
    id: int
    
    class Config:
        orm_mode = True
        
class Like(LikeBase):
    id: int
    
    class Config:
        orm_mode = True