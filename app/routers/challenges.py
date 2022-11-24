from typing import List

from fastapi import APIRouter, Depends

import app.schemas.challenge as challenge_schema
import app.cruds.challenge as challenge_crud

from app.db import get_db
router = APIRouter()


@router.get("/challenges", response_model=List[challenge_schema.Challenge])
async def list_challenges(db=Depends(get_db)):
    return challenge_crud.get_all_challenges(db=db)

@router.post("/challenges", response_model=challenge_schema.ChallengeCreateResponse)
async def create_challenge(challenge_body: challenge_schema.ChallengeCreate, db = Depends(get_db)):
    return challenge_crud.create_challenge(db=db, challenge_create=challenge_body)

@router.put("/challenges/{challenge_id}", response_model=challenge_schema.ChallengeCreateResponse)
async def update_challenge(challenge_id: int, challenge_body: challenge_schema.ChallengeCreate):
    return challenge_schema.ChallengeCreateResponse(id=challenge_id, **challenge_body.dict())

@router.delete("/challenges/{challenge_id}", response_model=None)
async def delete_challenge(challenge_id: int):
    pass