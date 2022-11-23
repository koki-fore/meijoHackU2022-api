from sqlalchemy.orm.session import Session

import app.models.user as user_model
import app.schemas.user as user_schema


def create_user(db: Session, user_create: user_schema.UserCreate) -> user_model.User: # DBモデルに変換
    user = user_model.User(**user_create.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user