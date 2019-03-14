# -*- coding:utf-8 -*-
'''
	创建数据
'''
from .dbsession import Base, engine

#将创建好的User类，映射到数据库的users表中
def run():
    print('------------create_all-------------')
    Base.metadata.create_all(engine)
    print('------------create_end-------------')

if __name__ == "__main__":
    run()