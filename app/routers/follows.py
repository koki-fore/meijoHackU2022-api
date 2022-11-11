from fastapi import APIRouter

router = APIRouter()


@router.get("/fallows")
async def list_fallows():
    pass

@router.post("/fallows")
async def create_fallow():
    pass

@router.put("/fallows/{fallow_id}")
async def update_fallow():
    pass

@router.delete("/fallows/{fallow_id}")
async def delete_fallow():
    pass