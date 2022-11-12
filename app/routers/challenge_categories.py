from typing import List

from fastapi import APIRouter

import app.schemas.challenge_category as challenge_category_schema

router = APIRouter()


@router.get("/challenge-categories", response_model=List[challenge_category_schema.Challenge_category])
async def list_challenge_category():
    pass

@router.post("/challenge-categories", response_model=challenge_category_schema.Challenge_category)
async def create_challenge_category(challenge_category_body: challenge_category_schema.Challenge_category):
    return challenge_category_schema.Challenge_category(**challenge_category_body.dict())

@router.delete("/challenge-categories/{challenge_category_id}", response_model=None)
async def delete_challenge_category(challenge_category_id: int):
    return