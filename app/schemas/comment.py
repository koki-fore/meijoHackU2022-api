from datetime import datetime
from pydantic import BaseModel

from .user import User
from .post import Post
# APIのリクエストやレスポンスの型を定義する

class CommentBase(BaseModel):
    user_FK: int
    post_FK: int
    text: str
    created_at: datetime
    updated_at: datetime
    
class CommentCreate(CommentBase):
    pass

class CommentCreateResponse(CommentBase):
    id: int
    
    class Config:
        orm_mode = True
        
class Comment(CommentBase):
    id: int
    
    user: User
    post: Post
    
    class Config:
        orm_mode = True