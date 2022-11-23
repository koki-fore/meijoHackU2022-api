from sqlalchemy.orm.session import Session

import app.models.follow as follow_model
import app.schemas.follow as follow_schema

def create_follow(db: Session, follow_create: follow_schema.FollowCreate) -> follow_model.Follow:
    follow=follow_model.Follow(**follow_create.dict())
    db.add(follow)
    db.commit()
    db.refresh(follow)

    return follow