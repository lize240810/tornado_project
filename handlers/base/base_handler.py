# -*- coding: utf-8 -*-
'''
    基层
    用户认证
'''
import tornado.web
import tornado.escape
import tornado.websocket

from libs.db.dbsession import db_session


class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        # 从cookie中获取用户姓名
        return self.get_secure_cookie("user")


# class MainHandler(BaseHandler):

#     def get(self):
#         if not self.current_user:
#             self.redirect("/login")
#             return
#         name = tornado.escape.xhtml_escape(self.current_user)
#         self.write("Hello, " + name)


# class LoginHandler(BaseHandler):

#     def get(self):
#         self.write('<html><body><form action="/login" method="post">'
#                    'Name: <input type="text" name="name">'
#                    '<input type="submit" value="Sign in">'
#                    '</form></body></html>')

#     def post(self):
#         self.set_secure_cookie("user", self.get_argument("name"))
