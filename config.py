# -*- coding: utf-8 -*-
'''
	整体配置文件
'''
import sys
import os

settings = dict(
	debug=True,
    static_path=os.path.join(os.getcwd(), 'static'),
    template_path=os.path.join(os.getcwd(), 'templates'),
	login_url="/login",  #重定向到登录页面
	cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
	xsrf_cookies=True, # 跨站伪造请求的防范
	pycket ={
        "engine": "redis",  # 配置存储类型
        "storage": {
            "host": "localhost",
            "port": 6379,
            "db_sessions": 5,
            "db_notifications": 11,
            "max_connections": 2 ** 31
        },
        "cookies": {
            "expires_days": 30,
            "max_age": 360
        }
    },
)

