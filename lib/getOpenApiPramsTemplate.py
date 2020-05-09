import time
from lib import getSignature

def get_url():
    """获得公用的url"""

    # url = 'http://api.heclouds.com:9090/oes/api/v1'
    # 测试环境地址
    url = 'https://test.api.heclouds.com/oes/api/v1'
    # return url

    # 韶钢线上环境
    # url = 'https://api.heclouds.com/oes/api/v1'
    # return url

    # 线上环境
    # url = 'https://api.heclouds.com/oes/api/v1'
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
    # 公网的accesskey
    # accessKey = 'Y3ESupiB9IGa9L90'

    # 测试环境
    accessKey = 'i11ebqvm0ZfzdjNk'
    return accessKey

def getAccessKeySecret():
    """获得公用的accessKeySecret参数"""
    # 公网环境
    # accessKeySecret = 'XM5Odos4fZd0ETqvGa6XjPZZVVBnSZdD7qcA'

    # 测试环境
    accessKeySecret = 'UvHCr4pEXj9ZJtVTXFCHqIwuJq3KfrWcB6eZ'
    return accessKeySecret

