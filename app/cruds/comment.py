from sqlalchemy.orm.session import Session

from typing import List
import app.models.comment as comment_model
import app.schemas.comment as comment_schema

def create_comment(db: Session, comment_create: comment_schema.CommentCreate) -> comment_model.Comment:
    comment=comment_model.Comment(**comment_create.dict())
    db.add(comment)
    db.commit()
    db.refresh(comment)

    return comment

def get_all_comment(db: Session) -> List[comment_model.Comment]:
    comments = db.query(comment_model.Comment).all()
    return comments