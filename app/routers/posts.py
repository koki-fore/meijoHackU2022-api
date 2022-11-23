from typing import List

from fastapi import APIRouter, Depends

import app.schemas.post as post_schema
import app.cruds.post as post_crud

from db import get_db
router = APIRouter()


@router.get("/posts", response_model=List[post_schema.Post])
async def list_posts():
    pass

@router.post("/posts", response_model=post_schema.PostCreateResponse)
async def create_post(post_body: post_schema.PostCreate, db = Depends(get_db)):
    return post_crud.create_post(db=db, post_create=post_body)

@router.put("/posts/{post_id}", response_model=post_schema.PostCreateResponse)
async def update_likes(post_id: int, like_count: int, post_body: post_schema.PostCreate):
    return post_schema.PostCreateResponse(id=post_id, like_count=like_count+1, **post_body.dict())

@router.delete("/posts/{post_id}", response_model=None)
async def delete_post(post_id: int):
    return