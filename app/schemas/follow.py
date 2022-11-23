from datetime import datetime
from pydantic import BaseModel

# APIのリクエストやレスポンスの型を定義する

class FollowBase(BaseModel):
    follower_id: int # followしている人
    followee_id: int # followされた人
    created_at: datetime
    updated_at:datetime

class FollowCreate(FollowBase):
    pass

class FollowCreateResponse(FollowBase):
    id: int
    
    class Config:
        orm_mode = True
        
class Follow(FollowBase):
    id: int
    
    class Config:
        orm_mode = True