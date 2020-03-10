import time
from lib import getSignature

def get_url():
    """获得公用的url"""
    url = 'http://api.heclouds.com:9090/oes/api/v1'
    return url

def getHeaders():
    """获取公用的headers数据"""
    headers = {
        'Content-Type': 'application/json',
        'platform': '2'
    }
    return headers

def getAccesskey():
    """获得公用的accessKey参数"""
    accessKey = 'jCTA6cduvIYINMs5'
    return accessKey

def getAccessKeySecret():
    """获得公用的accessKeySecret参数"""
    accessKeySecret = 'ytvAT2KIvIR3Cfs6l24njL9gFdIxllxhYXzM'
    return accessKeySecret

