from sqlalchemy.orm.session import Session

from typing import List
import app.models.like as like_model
import app.schemas.like as like_schema

def create_like(db: Session, like_create: like_schema.LikeCreate) -> like_model.Like:
    like=like_model.Like(**like_create.dict())
    db.add(like)
    db.commit()
    db.refresh(like)

    return like

def get_all_likes(db: Session) -> List[like_model.Like]:
    likes = db.query(like_model.Like).all()
    return likes