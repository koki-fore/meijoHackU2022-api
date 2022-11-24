from sqlalchemy.orm.session import Session

from typing import List
import app.models.user as user_model
import app.schemas.user as user_schema


def create_user(db: Session, user_create: user_schema.UserCreate) -> user_model.User: # DBモデルに変換
    user = user_model.User(**user_create.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_all_users(db: Session) -> List[user_model.User]:
    users = db.query(user_model.User).all()
    return users