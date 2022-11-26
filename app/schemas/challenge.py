from typing import List, Optional # Nullでも平気
from datetime import datetime
from pydantic import BaseModel, Field

from .post import Post
# APIのリクエストやレスポンスの型を定義する

class ChallengeBase(BaseModel):
    title: str
    text: Optional[str] = Field(None)
    experience_point: int = Field(0)
    
class ChallengeCreate(ChallengeBase):
    pass

class ChallengeCreateResponse(ChallengeBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True

class Challenge(ChallengeBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    posts: List[Post]
    
    class Config:
        orm_mode = True