from sqlalchemy.orm.session import Session

import app.models.comment as comment_model
import app.schemas.comment as comment_schema

def create_comment(db: Session, comment_create: comment_schema.Comment) -> comment_model.Comment:
    comment=comment_model.Comment(**comment_create.dict())
    db.add(comment)
    db.commit()
    db.refresh(comment)

    return comment