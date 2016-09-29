# -*- coding:utf-8 -*-

# __author__ = 'yuzhongfu'
# __mktime__ = '16/8/5'

from conf.settings import REDIS
from www.web.api.baseRequest import BaseRequest

class TestApi(BaseRequest):


    def get(self):

        data = self.__getData()

        self.renderApi(data)

    @BaseRequest.cacheRedis(REDIS.CACHE_TIMEOUT_1M)
    def __getData(self):

        return "testApi"


