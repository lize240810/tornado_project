# -*- coding:utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# 连接Mysql

HOST = '127.0.0.1'
PORT = '3306'
USERNAME = 'root'
PASSWORD = 'root'
DATABASE = 'test1'
MYSQL_INFO = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME,
    PASSWORD,
    HOST,
    PORT,
    DATABASE
)

# 创建引擎
engine = create_engine(MYSQL_INFO, echo=True)
# 创建基础
Base = declarative_base(engine)

db_session = scoped_session(
    sessionmaker(autocommit=False,
                 autoflush=False,
                 bind=engine))

Base.query = db_session.query_property()