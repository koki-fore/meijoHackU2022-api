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