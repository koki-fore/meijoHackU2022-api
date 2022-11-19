'''
DBの設定ファイル
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DB_URL = "mysql+pymysql://root@db:3306/meijoHackU2022-db?charset=utf8"
engine=create_engine(DB_URL)

sessionClass=sessionmaker(
    autocommit=False,autoflush=False,bind=engine
)

Base=declarative_base()

def get_db():
    return sessionClass()