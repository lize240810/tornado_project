# -*- coding:utf-8 -*-
import os
from uuid import uuid4
from datetime import datetime
from string import printable

import hashlib
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine, Column, Integer, String,
                        Text, Boolean, Date, DateTime, ForeignKey)

from libs.db.dbsession import Base, db_session


class User_model(Base):
    __tablename__ = 'user1'
    uuid = Column(String(36), unique=True,
                  nullable=False, default=str(uuid4()))
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(50), nullable=False)
    _password = Column('password', String(64))
    create_time = Column(DateTime, default=datetime.now().strftime('%F %T'))
    update_time = Column(DateTime)
    last_login = Column(DateTime)
    loginnum = Column(Integer, default=0)
    _locked = Column(Boolean, default=False, nullable=False)
    _avatar = Column(String(64))

    def _hash_password(self, password):
        hash_md5 = hashlib.md5()
        hash_md5.update(password.encode('utf-8'))
        hash_password = hash_md5.hexdigest()
        hash_md5.update(hash_password.encode('utf-8'))

        return str.__add__(hash_password, hash_md5.hexdigest())

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = self._hash_password(password)

    def auth_password(self, other_password):
        '''
            进行验证密码
            不正确返回False
        '''
        if self._password:
            return self.password == self._hash_password(other_password)
        else:
            return False

    @property
    def avatar(self):
        return self._avatar if self._avatar else "default_avatar.jpg"

    @avatar.setter
    def avatar(self, img_name):
        if img_name:
            self._avatar = img_name
        else:
            self._avatar = "default_avatar.jpg"
            


    @classmethod
    def all(cls):
        '''
            查询全部数据
        '''
        return db_session.query(cls).all()

    @classmethod
    def by_id(cls, id):
        '''
            根据自动增长的id查询数据
        '''
        return db_session.query(cls).filter_by(id=id).first()

    @classmethod
    def by_uuid(cls, uuid):
        '''
            更具uuid查询数据
        '''
        return db_session.query(cls).filter_by(uuid=uuid).first()

    @classmethod
    def by_name(cls, name):
        '''
            类方法
            根据用户名查询数据
            cls代表当前类
        '''
        return db_session.query(cls).filter_by(user_name=name).first()

    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, value):
        '''
            锁定用户
        '''
        assert isinstance(value, bool)
        self._locked = value

    def to_dict(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'last_login': self.last_login,
            'img_uri': self._avatar
        }

    def __repr__(self):
        return u'<User1 - id: %s  name: %s>' % (self.id, self.user_name)
