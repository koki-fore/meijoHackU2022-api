from sqlalchemy import create_engine
import os
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

'''
テーブル作成(すでに存在する場合は何もしない)
python create_db.pyで実行
'''
DB_URL = "mysql+pymysql://root@db:3306/meijoHackU2022-db?charset=utf8"
engine = create_engine(DB_URL, echo=True)

def create_database():
    Base.metadata.create_all(bind=engine)
    return 

if __name__=="__main__":
    create_database()