from fastapi import APIRouter

router = APIRouter()


@router.get("/challenge_categories")
async def list_challenge_category():
    pass

@router.post("/challenge_categories")
async def create_challenge_category():
    pass

@router.put("/challenge_categories/{challenge_category_id}")
async def update_challenge_category():
    pass

@router.delete("/challenge_categories/{challenge_category_id}")
async def delete_challenge_category():
    pass