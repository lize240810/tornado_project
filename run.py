# -*- coding:utf-8 -*-
'''
    项目主入口
'''
import os
import sys
sys.path.append(os.getcwd())

import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.escape
from tornado.options import define, options

from config import settings
# 导入路由
from handlers.main.main_urls import handlers
# 导入数据库
from libs.db import create_tables


#定义接口
define("port", default=8888, type=int, help="运行接口")
define("t", default=False, type=bool, help="是否创建表")

if __name__ == '__main__':
    options.parse_command_line() # 从命令行接受
    if options.t:
        create_tables.run()
    # 创建应用实例
    application = tornado.web.Application(handlers, **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.bind(options.port, '0.0.0.0')
    http_server.start()
    tornado.ioloop.IOLoop.instance().start()


