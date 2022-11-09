from typing import Optional # Nullでも平気
from datetime import datetime
from pydantic import BaseModel, Field

# APIのリクエストやレスポンスの型を定義する

class PostBase(BaseModel):
    id: int
    user_FK: int
    challenge_FK: Optional[int] = Field(None)
    text: str = Field(None, example='貯蓄用の水を買いました')
    picture_path_01: Optional[str] = Field(None)
    picture_path_02: Optional[str] = Field(None)
    picture_path_03: Optional[str] = Field(None)
    picture_path_04: Optional[str] = Field(None)
    like_count: Optional[int] = Field(0, example=100)
    created_at: datetime
    updated_at: datetime
    
class PostCreate(PostBase):
    pass
        
class PostCreateResponse(PostCreate):
    pass
    
    class Config:
        orm_mode = True

class Post(PostBase):
    pass
    
    class Config:
        orm_mode = True