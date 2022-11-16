from sqlalchemy import create_engine

from app.db import Base

from app.models.user import User
from app.models.category import Category
from app.models.challenge_category import Challenge_category
from app.models.challenge_completed import Challenge_completed
from app.models.challenge import Challenge
from app.models.comment import Comment
from app.models.follow import Follow
from app.models.like import Like
from app.models.post import Post


DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()