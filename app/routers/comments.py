from typing import List

from fastapi import APIRouter

import app.schemas.comment as comment_schema

router = APIRouter()


@router.get("/comments",response_model=List[comment_schema.Comment])
async def list_comments():
    pass

@router.post("/comments", response_model=comment_schema.Comment)
async def create_comment(comment_body: comment_schema.Comment):
    return comment_schema.Comment(**comment_body.dict())

@router.delete("/comments/{comment_id}", response_model=None)
async def delete_comment():
    return