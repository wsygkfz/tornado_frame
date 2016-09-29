# -*- coding:utf-8 -*-

# __author__ = 'yuzhongfu'
# __mktime__ = '16/8/5'


from tornado import gen

from conf.settings import REDIS

from www.controller.baseRequest import BaseRequest

class TestApi(BaseRequest):

    @gen.coroutine
    def get(self):
        data = yield self.__getData()
        print "===>-",data
        self.renderApi(data)

    @gen.coroutine
    @BaseRequest.cacheRedis(REDIS.CACHE_TIMEOUT_1M)
    def __getData(self):

        return "testApi"


