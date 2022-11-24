from typing import List

from fastapi import APIRouter, Depends, HTTPException,status

import app.cruds.user as user_crud
from app.db import get_db

import app.schemas.user as user_schema

router = APIRouter()


@router.get("/users", response_model=List[user_schema.User])
async def list_users(db = Depends(get_db)):
    return user_crud.get_all_users(db=db)

@router.get("/users/me")
async def get_user_me(current_user=Depends()):
    return current_user

@router.post("/users/", response_model=user_schema.UserCreateResponse)
async def create_user(user_body: user_schema.UserCreate, db = Depends(get_db)):
    return user_crud.create_user(db=db, user_create=user_body)

@router.put("/users/{user_id}", response_model=user_schema.UserCreateResponse)
async def update_user(user_id: int, experience_point_num: int, follower_num:int, followee_num: int, user_body: user_schema.UserCreate):
    return user_schema.UserCreateResponse(id=user_id, experience_point_num=experience_point_num, follower_num=follower_num, followee_num=followee_num, **user_body.dict())

@router.delete("/users/{user_id}", response_model=None)
async def delete_user(user_id: int):
    return