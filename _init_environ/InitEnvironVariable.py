# -*- coding:utf-8 -*-

# __author__ = 'yuzhongfu'
# __mktime__ = '16/8/15'

from redis  import Redis,ConnectionPool

from common.LogManager import get_logger
from common.NgMongo import NGMongoConnect

import conf.settings as settings
from conf.settings import LOGS,DBINFO,REDIS


# 初始化日志

class InitEnvironVariable():

    def __init__(self,args):

        self.__log_name = args.get("log_name")
        self.__log_level = args.get("log_level")
        self.__log_path = args.get("log_path")
        self.__log_show_stream = args.get("show_stream")

        # 初始化日志
        self.__init_loggr()
        # 初始化数据连接
        self.__init_mongodb()
        # 初始化redis
        self.__init_redis()

    def __init_redis(self):
        def conn_redis(**redis_conf):
            pool = ConnectionPool(**redis_conf)
            return Redis(connection_pool=pool)
        settings.g_redis = conn_redis(**REDIS.MACHINE)

    def __init_loggr(self):
        settings.g_logger = get_logger(
            strFileName = self.__log_name or LOGS.LOG_NAME,
            debug = self.__log_level or LOGS.LOG_LEVEL,
            showStreamLog = self.__log_show_stream or LOGS.LOG_SHOW_STREAM,
            saveLogPath = self.__log_path or LOGS.LOG_PATH
        )

    def __init_mongodb(self):


        # 密码是否为空时，数据连接拼接方式不一样
        if DBINFO.PASSWD:
            user_info = "%s:%s@"%(DBINFO.USER,DBINFO.PASSWD)
        else:
            user_info = ""

        master_host = "mongodb://%s%s:%d/%s"%(
            user_info,
            DBINFO.MASTER_IP,
            DBINFO.PORT,
            DBINFO.DB
        )
        slave_host = "mongodb://%s%s:%d/%s?slaveOk=true"%(
            user_info,
            DBINFO.SLAVE_IP,
            DBINFO.PORT,
            DBINFO.DB
        )

        # 主数据库连接
        mongo_master = NGMongoConnect(master_host)
        settings.g_master_db = mongo_master.get_database(DBINFO.DB)
        # 从数据库连接
        mongo_slave = NGMongoConnect(slave_host)
        settings.g_slave_db = mongo_slave.get_database(DBINFO.DB)


def init_environ_variable(args={}):
    """"""

    InitEnvironVariable(args)


if __name__ == "__main__":
    init_environ_variable()
    

