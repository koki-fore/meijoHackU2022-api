from typing import List

from fastapi import APIRouter, Depends

import app.schemas.follow as follow_schema
import app.cruds.follow as follow_crud

from app.db import get_db
router = APIRouter()


@router.get("/fallows", response_model=List[follow_schema.Follow])
async def list_fallows():
    pass

@router.post("/fallows", response_model=follow_schema.Follow)
async def create_fallow(follow_body: follow_schema.Follow, db=Depends(get_db)):
    return follow_crud.create_follow(db=db, follow_create=follow_body)

@router.delete("/fallows/{fallow_id}", response_model=None)
async def delete_fallow():
    return