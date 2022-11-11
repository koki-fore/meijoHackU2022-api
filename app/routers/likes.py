from fastapi import APIRouter

router = APIRouter()


@router.get("/likes")
async def list_categories():
    pass

@router.post("/likes")
async def create_category():
    pass

@router.put("/likes/{like_id}")
async def update_category():
    pass

@router.delete("/likes/{like_id}")
async def delete_category():
    pass