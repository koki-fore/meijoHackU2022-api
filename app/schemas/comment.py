from datetime import datetime
from pydantic import BaseModel

# APIのリクエストやレスポンスの型を定義する

class Comment(BaseModel):
    id: int
    user_FK: int
    post_FK: int
    text: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True