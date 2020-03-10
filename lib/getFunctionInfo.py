from urllib import parse
import time
import requests
import urllib3

from lib import getOpenApiPramsTemplate,getSignature,getGatewayProductInfo

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def getFunctionInfo():
    """获得创建的功能的信息"""
    pid = getGatewayProductInfo.getGatewayProductId()
    url = getOpenApiPramsTemplate.get_url() + '/products' + '/'+ str(pid) +'/properties'
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

def getFunctionId():
    """获取创建的功能ID"""
    r = getFunctionInfo()
    data = r.json()['data']
    fid = data[0].get('id')
    return fid

