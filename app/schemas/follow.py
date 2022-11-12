from datetime import datetime
from pydantic import BaseModel

# APIのリクエストやレスポンスの型を定義する

class Follow(BaseModel):
    id: int
    follower_id: int # followしている人
    followee_id: int # followされた人
    created_at: datetime
    updated_at:datetime
    
    class Config:
        orm_mode = True