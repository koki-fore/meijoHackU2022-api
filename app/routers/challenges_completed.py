from typing import List

from fastapi import APIRouter

import app.schemas.challenges_completed as challenges_completed_schema

router = APIRouter()


@router.get("/challenge-completed", response_model=List[challenges_completed_schema.Challenges_completed])
async def list_challenge_completed():
    pass

@router.post("/challenge-completed", response_model=challenges_completed_schema.Challenges_completed)
async def create_challenge_completed(challenges_completed_body: challenges_completed_schema.Challenges_completed):
    return challenges_completed_schema.Challenges_completed(**challenges_completed_body.dict())

@router.delete("/challenge-completed/{challenges_completed_id}", response_model=None)
async def delete_challenge_completed(challenges_completed_id: int):
    return