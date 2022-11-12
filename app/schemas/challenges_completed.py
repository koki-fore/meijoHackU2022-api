from datetime import datetime
from pydantic import BaseModel

# APIのリクエストやレスポンスの型を定義する

class Challenges_completed(BaseModel):
    id: int
    challenge_FK: int
    user_FK: int
    created_at: datetime
    updated_at:datetime
    
    class Config:
        orm_mode = True