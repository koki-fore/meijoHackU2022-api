from typing import List

from fastapi import APIRouter, Depends, HTTPException,status

import app.cruds.user as user_crud
from app.db import get_db

import app.schemas.user as user_schema

router = APIRouter()


@router.get("/users", response_model=List[user_schema.User])
async def list_users(db = Depends(get_db)):
    return user_crud.get_all_users(db=db)

@router.get("/users/me/{uid}", response_model=user_schema.User)
async def get_user_me(uid: str, db = Depends(get_db)):
    return user_crud.get_users_me(uid=uid ,db=db)

@router.post("/users/", response_model=user_schema.UserCreateResponse)
async def create_user(user_body: user_schema.UserCreate, db = Depends(get_db)):
    return user_crud.create_user(db=db, user_create=user_body)

@router.put("/users/{uid}", response_model=user_schema.UserCreateResponse)
async def update_user(user_id: str, user_body: user_schema.UserUpdate, db=Depends(get_db)):
    user = user_crud.get_users_me(db, uid=user_id)
    return user_crud.update_user(db, user_body, original=user)

@router.delete("/users/{user_id}", response_model=None)
async def delete_user(user_id: int):
    return