from sqlalchemy.orm.session import Session

import app.models.like as like_model
import app.schemas.like as like_schema

def create_like(db: Session, like_create: like_schema.Like) -> like_model.Like:
    like=like_model.Like(**like_create.dict())
    db.add(like)
    db.commit()
    db.refresh(like)

    return like