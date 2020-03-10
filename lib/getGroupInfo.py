from urllib import parse
import time
import requests
import urllib3
import json

from lib import getOpenApiPramsTemplate,getSignature,getGatewayProductInfo

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def getGroupInfo():
    """获得分组的信息"""
    pid = getGatewayProductInfo.getGatewayProductId()
    url = getOpenApiPramsTemplate.get_url() + '/label'
    accessKey = getOpenApiPramsTemplate.getAccesskey()
    accessKeySecret = getOpenApiPramsTemplate.getAccessKeySecret()
    headers = getOpenApiPramsTemplate.getHeaders()
    signatureNonce = int(time.time())

    params = {
        'accessKeyId': accessKey,
        'currentPage': '1',
        'name': 'g',
        'pageSize': '10',
        'product': pid,
        'signatureNonce': signatureNonce
    }
    body = {}
    signature = getSignature.get_signature(params, body, accessKeySecret, 'GET')
    params['signature'] = signature
    r = requests.get(url=url, params=params, headers=headers)
    return r

def getGroupId():
    """获得分组的id"""
    r = getGroupInfo()
    data = r.json()['data']
    content = data['content']
    group_id = content[0].get('id')
    return group_id


