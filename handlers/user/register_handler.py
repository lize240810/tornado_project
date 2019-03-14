# -*- coding:utf-8 -*-
'''
    用户注册
'''
import os
from hashlib import md5

import tornado.web
from handlers.base.base_handler import BaseHandler
from models.user_model import User_model
from libs.db.dbsession import db_session
import config


class RegisterHandler(BaseHandler):
    """用户注册处理器"""

    def get(self):
        self.render("user/register.html")

    def post(self):
        '''
                用户注册方法
        '''
        username = self.get_argument("name", default="", strip=True)
        password = self.get_argument("pass", default="", strip=True)
        # import ipdb; ipdb.set_trace()
        if not username:
            self.set_status(400)
            self.write({"message": "用户名不能为空"})
            return

        if not password:
            self.set_status(400)
            self.write({"message": "密码不能为空"})
            return
        search_user = User_model.by_name(username)
        if search_user:
            self.set_status(400)
            self.write({"message": u'用户名已被注册'})
            return
        # 创建新对象
        user = User_model()
        user.user_name = username
        # import ipdb; ipdb.set_trace()
        user.password = password
        user.avatar = self.uploadhandler
        db_session.add(user)
        try:
            db_session.commit()
            self.set_status(200)
            self.write({'message': '注册成功'})
        except Exception as e:
            db_session.rollback()
            self.set_status(400)
            self.write({'message': '注册失败'})

    @property
    def uploadhandler(self):
        '''
            把一个方法变化为属性
            图片上传
        '''
        files = self.request.files
        img_files = files.get('img')
        if not img_files:
            return
        img_file = img_files[0]["body"]
        # 创建唯一图片名
        md = md5()
        md.update(img_file)
        hash_img = '{}.jpg'.format(md.hexdigest())

        # 拼接图片名
        img_name = os.path.join(
            # 从配置中获取到路径名
            config.settings.get('static_path'),
            'images',
            hash_img
        )
        img_list = os.listdir(os.path.dirname(img_name))
        if not hash_img in img_list:
            # 保存图片
            with open(img_name, 'wb+') as file:
                file.write(img_file)
        return hash_img
