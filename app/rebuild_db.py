'''
dbのリセット・テーブル再作成
python rebuild_db.pyで実行
'''

from sqlalchemy import create_engine
import os
from db import Base
from models.user import User
from models.category import Category
from models.challenge_category import Challenge_category
from models.challenge_completed import Challenge_completed
from models.challenge import Challenge
from models.comment import Comment
from models.follow import Follow
from models.like import Like
from models.post import Post

DB_URL = "mysql://root@db:3306/meijoHackU2022-db?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()