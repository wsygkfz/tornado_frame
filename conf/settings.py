# -*- coding:utf-8 -*-

# __author__ = 'yuzhongfu'
# __mktime__ = '16/8/5'

import os
import logging
g_cur_process_run_path = os.getcwd()

g_root_path = os.path.dirname(os.path.realpath(__file__))
g_root_path = os.path.dirname(g_root_path)


# 静态文件路径
g_static_path = "www/static"
# 模板的路径
g_templates_path = "www/templates"

DEBUG_MODE = True
# tornado 的基本配置信息
settings = dict(
    template_path=os.path.join(g_root_path, g_templates_path),
    static_path=os.path.join(g_root_path, g_static_path),
    cookie_secret="bZJc2sWbQLKoscdGkHn/VytrsDuyhfkSsdSDajsR0kRvJ5/xJ89E=",
    login_url="/login",
    xsrf_cookies=True,
    debug=DEBUG_MODE,
)


# 日志相关配置
# 日志句柄
g_logger = None
class LOGS():

    # 文件名
    LOG_NAME = "api_web.log"
    # 日志级别
    LOG_LEVEL = logging.ERROR
    # 是否输出到屏幕
    LOG_SHOW_STREAM = True
    # 日志存放目录
    LOG_PATH = g_cur_process_run_path


# 主从数据连接句柄
g_master_db = None
g_slave_db = None
class DBINFO:

    if DEBUG_MODE:
        #  local 只为测试使用
        MASTER_IP = "127.0.0.1"
        SLAVE_IP = "127.0.0.1"
        PORT = 27017
        USER = ""
        PASSWD = ""
    else:
        # 国外数据库主库IP
        MASTER_IP = ""
        # 国外数据库从库IP
        SLAVE_IP = ""
        PORT = 47077
        USER = ""
        PASSWD = ""
    DB = "mallcenter"


class STATUS_CODE:
    # 执行成功
    SUCCESS = 200
    # 执行失败
    FAILED =  400
    # 服务异常
    ERROR = 500



# 缓存redis
g_redis = None
class REDIS:

    # redis的相关机器信息
    if DEBUG_MODE:
        MACHINE = {
            "host": "127.0.0.1",
            "port": 6380,
            "password": "jm*7yrt@13",
            "db": 6
        }
    else:
        MACHINE = {
            "host": "127.0.0.1",
            "port": 6380,
            "password": "jm*7yrt@13",
            "db": 6
            }


    # 分别缓存的单位时间（秒）
    CACHE_TIMEOUT_10S  = 10
    CACHE_TIMEOUT_30S  = 30
    CACHE_TIMEOUT_1M  = 60
    CACHE_TIMEOUT_5M  = 5 * 60
    CACHE_TIMEOUT_10M = 10 * 60
    CACHE_TIMEOUT_30M = 30 * 60
    CACHE_TIMEOUT_1H  = 60 * 60
    CACHE_TIMEOUT_2H  = 2 * 60 * 60
    CACHE_TIMEOUT_5H  = 5 * 60 * 60
    CACHE_TIMEOUT_1D  = 24 * 60 * 60
    CACHE_TIMEOUT_1W  = 7 * 24 * 60 * 60


class LOCAL_HOST:
    # 启动服务器的地址
    HTTP_API_HOST_IP = "0.0.0.0"
    HTTP_API_HOST_PORT = 8888


# 语言对应的国家
g_dict_app_country = {
    # 中国
    "zh_hant_hk": "CN", "zh_hans_hk": "CN",
    "zh_hant_tw": "CN", "zh_hans_tw": "CN",
    "zh_hant_mo": "CN", "zh_hans_mo": "CN",
    "zh_hant_sg": "CN", "zh_hans_sg": "CN",

    "zh_hans": "CN","zh": "CN","zh_hans": "CN",

    # 美国
    "us": "US",
    "en": "US",
    # 阿拉伯
    'ar_ye':"SA",'ar_eg':"SA",'ar_sa':"SA",'ar_sd':"SA",'ar_ly':"SA",'ar_om':"SA",'ar_ma':"SA",
    'ar_tn':"SA",'ar_jo':"SA",'ar_ae':"SA",'ar_dz':"SA",'ar_sy':"SA",'ar_iq':"SA",'ar_bh':"SA",
    'ar_kw':"SA",'ar_qa':"SA",'ar_lb':"SA",'ar':"SA",

    # 英国
    "kw_gb":"GB","en_gb":"GB","cy_gb":"GB","gv_gb":"GB",
    # 法国
    'fr_gp':"FR", 'fr_gq':"FR", 'fr_rw':"FR", 'fr_td':"FR", 'fr_km':"FR", 'fr_tg':"FR", 'fr_lu':"FR",
    'fr_ne':"FR", 'fr_ca':"FR", 'fr_dj':"FR", 'fr_mc':"FR", 'fr_cd':"FR", 'fr_cf':"FR", 'fr_re':"FR",
    'fr_cg':"FR", 'fr_mg':"FR", 'fr_ga':"FR", 'fr_ch':"FR", 'fr_sn':"FR", 'fr_ci':"FR", 'fr_be':"FR",
    'fr_bf':"FR", 'fr_ml':"FR", 'fr_cm':"FR", 'fr_bi':"FR", 'fr_bj':"FR", 'fr_mq':"FR", 'fr_bl':"FR",
    'fr_fr':"FR", 'fr_mf':"FR", 'fr_gn':"FR", 'fr':"FR",

    # 加拿大
    "en_ca":"CA","fr_ca":"CA",
    # 日本
    "ja":"JP","ja_jp":"JP",
    # 西班牙
    "es_hn":"ES","es_co":"ES","es_pa":"ES","es_cr":"ES","es_sv":"ES","es_pe":"ES","es_uy":"ES","es_do":"ES",
    "es_bo":"ES","es_ec":"ES","es_gq":"ES","es_gt":"ES","es_ar":"ES","es_cl":"ES","es_ve":"ES","es_co":"ES",
    "es_pr":"ES","es_us":"ES","es_es":"ES","es":"ES","es_419":"ES","es_py":"ES","es_ni":"ES",
    # 俄罗斯
    "ru":"RU",
    # 荷兰
    'nl':"NL", 'nl_nl':"NL", 'nl_be':"NL",
    # 葡萄牙
    'pt_br':"PT", 'pt_mz':"PT", 'pt_gw':"PT", 'pt_pt':"PT", 'pt':"PT",
    # 土耳其
    "tr":"TR",
    # 墨西哥
    "es_mx":"MX",
}

def start():
    """"""


if __name__ == "__main__":
    start()
    
