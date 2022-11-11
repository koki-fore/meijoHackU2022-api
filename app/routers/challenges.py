from fastapi import APIRouter

router = APIRouter()


@router.get("/challenges")
async def list_challenges():
    pass

@router.post("/challenges")
async def create_challenge():
    pass

@router.put("/challenges/{challenge_id}")
async def update_challenge():
    pass

@router.delete("/challenges/{challenge_id}")
async def delete_challenge():
    pass