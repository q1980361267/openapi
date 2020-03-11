from urllib import parse
import time
import requests
import urllib3

from lib import getOpenApiPramsTemplate,getSignature,getGatewayProductInfo

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def getGatewayDevicesInfo():
    """获得创建的网关设备的信息"""
    url = getOpenApiPramsTemplate.get_url() + '/devices/multi'
    accessKey = getOpenApiPramsTemplate.getAccesskey()
    accessKeySecret = getOpenApiPramsTemplate.getAccessKeySecret()
    headers = getOpenApiPramsTemplate.getHeaders()
    signatureNonce = int(time.time())
    productId = getGatewayProductInfo.getGatewayProductId()
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

def getGatewayDevicesId():
    """获得创建的网关产品的id"""
    r = getGatewayDevicesInfo()
    data = r.json()['data']
    content = data['content']
    dev_id = content[0].get('id')
    # print(dev_id)
    return dev_id

def getGatewayDevicesIdSecond():
    """获得创建的网关产品的id"""
    r = getGatewayDevicesInfo()
    data = r.json()['data']
    content = data['content']
    dev_id_second = content[1].get('id')
    # print(dev_id_second)
    return dev_id_second

def getGatewayDevicesIdThird():
    """获得创建的网关产品的id"""
    r = getGatewayDevicesInfo()
    data = r.json()['data']
    content = data['content']
    dev_id_third = content[2].get('id')
    # print(dev_id_second)
    return dev_id_third

def getGatewayDevicesApikey():
    r = getGatewayDevicesInfo()
    data = r.json()['data']
    content = data['content']
    dev_ak = content[0].get('apiKey')
    return dev_ak
# getGatewayDevicesId()
# getGatewayDevicesIdSecond()
# getGatewayDevicesIdThird()


