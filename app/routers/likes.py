from typing import List

from fastapi import APIRouter, Depends

import app.schemas.like as like_schema
import app.cruds.like as like_crud

from db import get_db
router = APIRouter()


@router.get("/likes", response_model=List[like_schema.Like])
async def list_likes():
    pass

@router.post("/likes", response_model=like_schema.LikeCreateResponse)
async def create_like(like_body: like_schema.LikeCreate, db=Depends(get_db)):
    return like_crud.create_like(db=db, like_create=like_body)

@router.delete("/likes/{like_id}", response_model=None)
async def delete_like():
    return