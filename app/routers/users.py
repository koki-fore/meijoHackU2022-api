from typing import List

from fastapi import APIRouter

import app.schemas.user as user_schema

router = APIRouter()


@router.get("/users", response_model=List[user_schema.User])
async def list_users():
    pass

@router.get("/users/me")
async def get_user_me():
    pass

@router.get("/users/{user_id}")
async def get_user():
    pass

@router.post("/users/", response_model=user_schema.UserCreateResponse)
async def create_user(user_body: user_schema.UserCreate):
    return user_schema.UserCreateResponse(id=1, experience_point_num=0, followee_num=0, follower_num=0, **user_body.dict())

@router.put("/users/{user_id}", response_model=user_schema.UserCreateResponse)
async def update_user(user_id: int, experience_point_num: int, follower_num:int, followee_num: int, user_body: user_schema.UserCreate):
    return user_schema.UserCreateResponse(id=user_id, experience_point_num=experience_point_num, follower_num=follower_num, followee_num=followee_num, **user_body.dict())

@router.delete("/users/{user_id}", response_model=None)
async def delete_user(user_id: int):
    return