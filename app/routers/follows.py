from typing import List

from fastapi import APIRouter

import app.schemas.follow as follow_schema

router = APIRouter()


@router.get("/fallows", response_model=List[follow_schema.Follow])
async def list_fallows():
    pass

@router.post("/fallows", response_model=follow_schema.Follow)
async def create_fallow(follow_body: follow_schema.Follow):
    return follow_schema.Follow(**follow_body.dict())

@router.delete("/fallows/{fallow_id}", response_model=None)
async def delete_fallow():
    return