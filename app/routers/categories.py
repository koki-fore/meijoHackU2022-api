from typing import List

from fastapi import APIRouter

import app.schemas.category as category_schema

router = APIRouter()


@router.get("/categories", response_model=List[category_schema.Category])
async def list_categories():
    pass

@router.post("/categories", response_model=List[category_schema.CategoryCreateResponse])
async def create_category(category_body: category_schema.CategoryBase):
    return category_schema.CategoryCreateResponse(**category_body.dict())

@router.put("/categories/{category_id}", response_model=List[category_schema.CategoryCreateResponse])
async def update_category(category_body: category_schema.CategoryBase):
    return category_schema.CategoryCreateResponse(**category_body.dict())

@router.delete("/categories/{category_id}", response_model=None)
async def delete_category(category_id: int):
    pass