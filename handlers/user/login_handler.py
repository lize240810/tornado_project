# -*- coding:utf-8 -*-
'''
    用户登录模块
'''
from datetime import datetime

import tornado.web
from handlers.base.base_handler import BaseHandler
from models.user_model import User_model
from libs.db.dbsession import db_session


class LoginHandler(BaseHandler):
    """用户登录模块"""

    def get(self):
        if not self.get_secure_cookie("user"):
            self.render(r"user\login.html")
            return 

        user_out = self.get_argument("op", "")
        if user_out == "login_out" and self.get_secure_cookie("user"):
            self.clear_all_cookies()
            self.set_status(200, "login_out sucess")
            self.write({'message': '注销成功'})
        self.redirect(r'/')

    def post(self):
        # import ipdb; ipdb.set_trace()
        username = self.get_argument("username", "", strip=True)
        password = self.get_argument("password", "", strip=True)

        # 根据用户名去查询数据库
        search_user = User_model.by_name(username)

        if search_user and search_user.auth_password(password):
            self.success_login(search_user)
            self.set_status(200)
            # self.write({'message': '登录成功'})
            self.redirect('/')
        else:
            self.set_status(400, "login error")
            self.write({'message': '登录失败'})

    def success_login(self, user):
        '''
            登录以后修改的属性
        '''
        # 最后一次登录时间
        user.last_login = datetime.now().strftime('%F %T')
        # 登录次数+1
        user.loginnum += 1
        # 存储到数据
        db_session.add(user)
        db_session.commit()
        # import ipdb; ipdb.set_trace()
        # 查询数据库存在就添加到cookie中
        self.set_secure_cookie("user", str(user.to_dict()), expires_days=5)
