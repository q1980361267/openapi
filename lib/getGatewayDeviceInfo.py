# coding:gbk
from urllib import parse
import time
import requests
import urllib3

from lib import getOpenApiPramsTemplate,getSignature,getGatewayProductInfo

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def getDevicesInfo():
    """获得创建的网关设备的信息"""
    url = getOpenApiPramsTemplate.get_url() + '/devices/multi'
    accessKey = getOpenApiPramsTemplate.getAccesskey()
    accessKeySecret = getOpenApiPramsTemplate.getAccessKeySecret()
    headers = getOpenApiPramsTemplate.getHeaders()
    signatureNonce = int(time.time())
    # 获取网关产品ID
    productId = getGatewayProductInfo.getGatewayProductIdSecond()
    params = {
        'accessKeyId': accessKey,
        'currentPage': '1',
        'pageSize': '10',
        'signatureNonce': signatureNonce,
        'productId' : productId
    }
    body = {}
    signature = getSignature.get_signature(params, body, accessKeySecret, 'GET')
    params['signature'] = signature
    r = requests.get(url=url, params=params, headers=headers)
    # print(r.json())
    return r

def getDevicesId():
    """获得创建的网关产品的id"""
    r = getDevicesInfo()
    data = r.json()['data']
    content = data['content']
    dev_id = content[0].get('id')
    # print(dev_id)
    return dev_id

def getGatewayDevicesApikey():
    r = getDevicesInfo()
    data = r.json()['data']
    content = data['content']
    dev_ak = content[0].get('apiKey')
    return dev_ak
# getGatewayDevicesId()
# getGatewayDevicesIdSecond()
# getGatewayDevicesIdThird()
# getDevicesInfo()

