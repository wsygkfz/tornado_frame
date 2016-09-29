# -*- coding:utf-8 -*-

# __author__ = 'yuzhongfu'
# __mktime__ = '16/8/30'


from www.controller.api.testApi import TestApi

from www.controller.website.testWeb import TestWeb


api_urls = [

    (r"/api", TestApi),

    (r"/", TestWeb),
    (r"/web", TestWeb),

]

def start():
    """"""


if __name__ == "__main__":
    start()
    

