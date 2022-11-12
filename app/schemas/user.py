from typing import Optional # Nullでも平気
from datetime import datetime
from pydantic import BaseModel, Field

# APIのリクエストやレスポンスの型を定義する

class UserBase(BaseModel):
    firebase_FK: int
    user_id: str
    screen_name: str
    first_name: str
    last_name: str
    picture_description: Optional[str] = Field(None, example='初めまして')
    created_at: datetime
    updated_at: datetime

class UserCreate(UserBase):
    pass

class UserCreateResponse(UserBase):
    id: int
    experience_point_num : Optional[int] = Field(0)
    follower_num:int = Field(0)
    followee_num:int = Field(0)
    
    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    experience_point_num : Optional[int] = Field(0)
    follower_num:int = Field(0)
    followee_num:int = Field(0)
    
    class Config:
        orm_mode = True