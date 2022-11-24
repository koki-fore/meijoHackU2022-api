from typing import List

from fastapi import APIRouter, Depends

import app.schemas.comment as comment_schema
import app.cruds.comment as comment_crud

from app.db import get_db
router = APIRouter()


@router.get("/comments",response_model=List[comment_schema.Comment])
async def list_comments(db=Depends(get_db)):
    return comment_crud.get_all_comment(db=db)

@router.post("/comments", response_model=comment_schema.CommentCreateResponse)
async def create_comment(comment_body: comment_schema.CommentCreate, db=Depends(get_db)):
    return comment_crud.create_comment(db=db, comment_create=comment_body)

@router.delete("/comments/{comment_id}", response_model=None)
async def delete_comment():
    return