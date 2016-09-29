# -*- coding:utf-8 -*-

# __author__ = 'yuzhongfu'
# __mktime__ = '16/8/5'


import json
import time
import traceback
import tornado.web

from conf.settings import g_logger,g_redis


class BaseRequest(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs):

        super(BaseRequest, self).__init__(application, request, **kwargs)

        self._callback = self.get_argument("callback", "")

        self._language = self.get_argument("language", "en")

        # 设置cookies的变量
        self.__cookies = {}


    def _getRedisKey(self):
        return self.request.uri


    @staticmethod
    def cacheRedis(cache_time):
        def wrapsFun(func):
            def __wrapsFun(*args, **kwargs):
                #每一个请求的URL参数组成的键值
                redis_key = args[0]._getRedisKey()
                # 先从redis获取对应的结果,有值直接返回
                try:
                    redis_content = g_redis.get(redis_key)
                    if redis_content:
                        return json.loads(redis_content)
                except:
                    g_logger.error(traceback.format_exc())
                # 如果redis没有值，按对应的请求获取结果
                redis_content = func(*args, **kwargs)
                try:
                    # 保存结果到redis中
                    g_redis.setex(redis_key, json.dumps(redis_content), cache_time)
                except:
                    g_logger.error(traceback.format_exc())
                return redis_content

            return __wrapsFun

        return wrapsFun


    def renderApi(self, data="",page_info={}):
        """
        """
        return_data = {
            "code": 200,
            "time": time.time() - self.request._start_time,
            "data": {
                "results": data,
                "pageInfo": page_info,
            }
        }
        if self._callback:
            return_data = self._callback + "(" + json.dumps(return_data) + ")"

        self.write(return_data)

        self.finish()

    def _set_cookies(self,dict_cookies):

        try:
            if type(dict_cookies).__name__ == "dict":
                self.__cookies.update(dict_cookies)
            return True
        except:
            g_logger.error(traceback.format_exc())
        return False

    def _render_template(self,template,**kwargs):

        try:
            # 设置cookies
            for key,value in  self.__cookies.items():
                self.set_cookie(key,value)
            self.render(template,**kwargs)
        except:
            g_logger.error(traceback.format_exc())


    def write_error(self, status_code, **kwargs):
        g_logger.error(traceback.format_exc())
        return_data = {
            "code": 500,
            "time": time.time() - self.request._start_time,
            "data": {
                "results": [],
            }
        }
        self.write(return_data)
        self.finish()

    def data_received(self, chunk):
        pass