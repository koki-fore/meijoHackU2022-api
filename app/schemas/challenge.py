from typing import Optional # Nullでも平気
from datetime import datetime
from pydantic import BaseModel, Field

# APIのリクエストやレスポンスの型を定義する

class ChallengeBase(BaseModel):
    category_FK: int
    title: str
    text: Optional[str] = Field(None)
    experience_point: int = Field(0)
    created_at: datetime
    updated_at: datetime
    
class ChallengeCreate(ChallengeBase):
    pass

class ChallengeCreateResponse(ChallengeBase):
    id: int
    
    class Config:
        orm_mode = True

class Challenge(ChallengeBase):
    id: int
    
    class Config:
        orm_mode = True