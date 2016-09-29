# -*- coding:utf-8 -*-

# __author__ = 'yuzhongfu'
# __mktime__ = '16/8/5'


# 程序启动时初始化全局属性
from _init_environ.InitEnvironVariable import init_environ_variable
init_environ_variable()

# 系统库
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

#自己定义库
from conf.settings import settings
from routeUrls import urls

define("port", default=8000, help="run on the given port", type=int)
application = tornado.web.Application(
    handlers = urls,
    **settings
)


def start_process():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application, xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':

    start_process()

