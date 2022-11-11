from fastapi import APIRouter

router = APIRouter()


@router.get("/challenge-categories")
async def list_challenge_category():
    pass

@router.post("/challenge-categories")
async def create_challenge_category():
    pass

@router.put("/challenge-categories/{challenge_category_id}")
async def update_challenge_category():
    pass

@router.delete("/challenge-categories/{challenge_category_id}")
async def delete_challenge_category():
    pass