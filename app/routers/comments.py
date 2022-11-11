from fastapi import APIRouter

router = APIRouter()


@router.get("/comments")
async def list_comments():
    pass

@router.post("/comments")
async def create_comment():
    pass

@router.put("/comments/{comment_id}")
async def update_comment():
    pass

@router.delete("/comments/{comment_id}")
async def delete_comment():
    pass