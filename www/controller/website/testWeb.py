# -*- coding:utf-8 -*-

# __author__ = 'yuzhongfu'
# __mktime__ = '16/8/5'


from tornado import gen

from conf.settings import REDIS

from www.controller.baseRequest import BaseRequest


def auth_token(func):
    """
    token验证装饰器
    :param func:
    :return:
    """
    def inner(self, *args, **kwargs):
        value = 11
        if value == str(self.user_id):
            return func(self, *args, **kwargs)
        else:
            self.return_by_json(code=10000, results=11)
    return inner

class TestWeb(BaseRequest):

    @gen.coroutine
    def get(self):
        data = yield self.__getData()
        import time
        self._set_cookies({"name":str(time.time())})
        self._render_template("website/index.html",data=data)

    @gen.coroutine
    @BaseRequest.cacheRedis(REDIS.CACHE_TIMEOUT_1M)
    def __getData(self):
        return {"key":"testApi"}


