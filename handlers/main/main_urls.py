'''
	路由注册页
'''
from .main_handler import MainHandler
from handlers.user.user_urls import user_urls
handlers = [
    (r'/', MainHandler),
]

handlers.extend(user_urls)
