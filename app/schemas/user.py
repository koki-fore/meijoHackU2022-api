from typing import List, Optional # Nullでも平気
from datetime import datetime
from pydantic import BaseModel, Field
# from .post import Post
from .challenges_completed import Challenge_completed
from .comment import Comment

# APIのリクエストやレスポンスの型を定義する

class UserBase(BaseModel):
    firebase_FK: str
    user_id: Optional[str] = Field(None)
    screen_name: Optional[str] = Field(None)
    first_name: Optional[str] = Field(None)
    last_name: Optional[str] = Field(None)
    profile_picture_path: Optional[str] = Field(None)
    description: Optional[str] = Field(None, example='初めまして')
    
    # class Config:
    #     orm_mode=True

class UserCreate(UserBase):
    pass

    class Config:
        orm_mode = True
    
class UserCreateResponse(UserBase):
    id: int
    experience_point_num : Optional[int] = Field(0)
    follower_num:int = Field(0)
    followee_num:int = Field(0)
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    experience_point_num : Optional[int] = Field(0)
    follower_num:int = Field(0)
    followee_num:int = Field(0)
    created_at: datetime
    updated_at: datetime
    # posts: List[Post]
    comments: List[Comment]
    challenge_completed: List[Challenge_completed]
    
    class Config:
        orm_mode = True