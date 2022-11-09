from typing import List

from fastapi import APIRouter

import app.schemas.posts as post_schema

router = APIRouter()


@router.get("/posts", response_model=List[post_schema.Post])
async def list_posts():
    return [post_schema.Post(id=1, text='水を買ったよ')]  # type: ignore

@router.post("/posts", response_model=post_schema.PostCreateResponse)
async def create_post(post_body: post_schema.PostCreate):
    return post_schema.PostCreateResponse(**post_body.dict())
    

@router.put("/posts/{post_id}", response_model=None)
async def update_likes(post_id: int):
    return