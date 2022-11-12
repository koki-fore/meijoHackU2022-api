from typing import List

from fastapi import APIRouter

import app.schemas.like as like_schema

router = APIRouter()


@router.get("/likes", response_model=List[like_schema.Like])
async def list_likes():
    pass

@router.post("/likes", response_model=like_schema.Like)
async def create_like(like_body: like_schema.Like):
    return like_schema.Like(**like_body.dict())

@router.delete("/likes/{like_id}", response_model=None)
async def delete_like():
    return