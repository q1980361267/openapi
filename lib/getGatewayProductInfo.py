from urllib import parse
import time
import requests
import urllib3

from lib import getOpenApiPramsTemplate,getSignature

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def getGatewayProductInfo():
    """获得创建的网关节点产品的信息"""
    url = getOpenApiPramsTemplate.get_url() + '/products'
    accessKey = getOpenApiPramsTemplate.getAccesskey()
    accessKeySecret = getOpenApiPramsTemplate.getAccessKeySecret()
    headers = getOpenApiPramsTemplate.getHeaders()
    signatureNonce = int(time.time())

    params = {
        'accessKeyId': accessKey,
        'currentPage': '1',
        'pageSize': '10',
        'signatureNonce': signatureNonce
    }
    body = {}
    signature = getSignature.get_signature(params, body, accessKeySecret, 'GET')
    params['signature'] = signature
    r = requests.get(url=url, params=params, headers=headers)
    # print(r.json())
    return r

def getGatewayProductId():
    """获得创建的网关产品的id"""
    r = getGatewayProductInfo()
    data = r.json()['data']
    content = data['content']
    pid = content[0].get('id')
    # print(pid)
    return pid

def getGatewayProductIdSecond():
    """获得创建的网关产品的id"""
    r = getGatewayProductInfo()
    data = r.json()['data']
    content = data['content']
    pid_second = content[1].get('id')
    # print(pid_second)
    return pid_second

def getGatewayProductMasterkey():
    r = getGatewayProductInfo()
    data = r.json()['data']
    content = data['content']
    pro_mk = content[0].get('masterKey')
    return pro_mk
# getGatewayProductId()
# getGatewayProductIdSecond()