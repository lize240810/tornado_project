'''
	主程序
'''
import datetime
import tornado.web
from handlers.base.base_handler import BaseHandler


class MainHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        # import ipdb; ipdb.set_trace()
        #从cookie中获取
        user = eval(self.get_secure_cookie("user").decode("utf-8"))
        # 渲染页面时传入
        self.render("main/index.html", user=user)
