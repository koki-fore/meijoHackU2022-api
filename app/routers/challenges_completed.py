from fastapi import APIRouter

router = APIRouter()


@router.get("/challenge_completed")
async def list_challenge_completed():
    pass

@router.post("/challenge_completed")
async def create_challenge_completed():
    pass

@router.put("/challenge_completed/{challenge_completed_id}")
async def update_challenge_completed():
    pass

@router.delete("/challenge_completed/{challenge_completed_id}")
async def delete_challenge_completed():
    pass