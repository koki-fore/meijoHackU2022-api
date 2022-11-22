from sqlalchemy.orm.session import Session

import app.models.category as category_model
import app.schemas.category as category_schema

def create_category(db: Session, category_create: category_schema.CategoryCreate) -> category_model.Category:
    category=category_model.Category(**category_create.dict())
    db.add(category)
    db.commit()
    db.refresh(category)

    return category