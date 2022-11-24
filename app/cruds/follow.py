from sqlalchemy.orm.session import Session

from typing import List
import app.models.follow as follow_model
import app.schemas.follow as follow_schema

def create_follow(db: Session, follow_create: follow_schema.FollowCreate) -> follow_model.Follow:
    follow=follow_model.Follow(**follow_create.dict())
    db.add(follow)
    db.commit()
    db.refresh(follow)

    return follow

def get_all_follows(db: Session) -> List[follow_model.Follow]:
    follows = db.query(follow_model.Follow).all()
    return follows