from sqlalchemy.orm.session import Session

import app.models.post as post_model
import app.schemas.post as post_schema

def create_post(db: Session, post_create: post_schema.PostCreate) -> post_model.Post:
    post=post_model.Post(**post_create.dict())
    db.add(post)
    db.commit()
    db.refresh(post)

    return post