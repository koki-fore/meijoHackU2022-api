from fastapi import APIRouter

router = APIRouter()


@router.get("/categories")
async def list_categories():
    pass

@router.post("/categories")
async def create_category():
    pass

@router.put("/categories/{category_id}")
async def update_category():
    pass

@router.delete("/categories/{category_id}")
async def delete_category():
    pass