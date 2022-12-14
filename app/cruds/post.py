from sqlalchemy.orm.session import Session

from typing import List
import app.models.post as post_model
import app.schemas.post as post_schema

def create_post(db: Session, post_create: post_schema.PostCreate) -> post_model.Post:
    post=post_model.Post(**post_create.dict())
    db.add(post)
    db.commit()
    db.refresh(post)

    return post

def get_all_posts(db: Session) -> List[post_model.Post]:
    posts = db.query(post_model.Post).all()
    return posts

def get_post(db: Session, id: int) -> post_model.Post:
    post = db.query(post_model.Post).filter(post_model.Post.id==id).one_or_none()
    return post

def delete_post(db: Session, original: post_model.Post) -> None:
    db.delete(original)
    db.commit()