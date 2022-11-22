from typing import List

from fastapi import APIRouter, Depends

import app.schemas.challenges_completed as challenges_completed_schema
import app.cruds.challenge_completed as challenge_completed_crud

from app.db import get_db
router = APIRouter()


@router.get("/challenge-completed", response_model=List[challenges_completed_schema.Challenges_completed])
async def list_challenge_completed():
    pass

@router.post("/challenge-completed", response_model=challenges_completed_schema.Challenges_completed)
async def create_challenge_completed(challenges_completed_body: challenges_completed_schema.Challenges_completed, db=Depends(get_db)):
    return challenge_completed_crud.create_challenge_completed(db=db, challenge_completed_create=challenges_completed_body)

@router.delete("/challenge-completed/{challenges_completed_id}", response_model=None)
async def delete_challenge_completed(challenges_completed_id: int):
    return