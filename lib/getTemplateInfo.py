# coding:gbk
from urllib import parse
import time
import requests
import urllib3

from lib import getOpenApiPramsTemplate,getSignature,getGatewayProductInfo

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def getTemplateInfo():
    """获得模板的信息"""
    url = getOpenApiPramsTemplate.get_url() + '/objtemplate/page'
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

def getTemplateId():
    """获得创建的网关产品的id"""
    r = getTemplateInfo()
    data = r.json()['data']
    content = data['content']
    template_id = content[0].get('id')
    # print(dev_id)
    return template_id


# getGatewayDevicesId()
# getGatewayDevicesIdSecond()
# getGatewayDevicesIdThird()
# getTemplateInfo()
# getTemplateId()