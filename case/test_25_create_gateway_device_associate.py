# coding:gbk
from urllib import parse
import unittest
import time
import requests
import logging
import urllib3
import json

from lib import getOpenApiPramsTemplate, getSignature, getDeviceInfo, getGatewayProductInfo,getGatewayDeviceInfo


class Test_CreateGatewayDeviceAssociate(unittest.TestCase):
    """创建网关设备关联接口"""

    # 类执行前初始
    @classmethod
    def setUpClass(cls):
        # 关闭https的证书校验
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    @classmethod
    def tearDownClass(cls):
        pass

    # 方法前初始
    def setUp(self):
        self.id_pro = getGatewayProductInfo.getGatewayProductId()
        self.id_dev_first = getDeviceInfo.getGatewayDevicesId()
        self.id_dev_second = getDeviceInfo.getGatewayDevicesIdSecond()
        self.id_gateway = getGatewayDeviceInfo.getDevicesId()
        self.url = getOpenApiPramsTemplate.get_url() + '/devices/gateway/associations'
        self.accessKey = getOpenApiPramsTemplate.getAccesskey()
        self.accessKeySecret = getOpenApiPramsTemplate.getAccessKeySecret()
        self.headers = getOpenApiPramsTemplate.getHeaders()
        self.signatureNonce = int(time.time())

    def tearDown(self):
        pass

    def test_00(self):  # 执行逻辑::设置入参，参数正确填写
        """创建网关设备关联-成功"""
        params = {
            'accessKeyId': self.accessKey,
            'deviceIds': [self.id_dev_first, self.id_dev_second],
            'gatewayId': self.id_gateway,
            'productId': self.id_pro,
            'signatureNonce': self.signatureNonce
        }
        body = {

        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=self.url, params=params, data=json.dumps(body), headers=self.headers)
        # success = r.json()['success']
        # 对响应的结果进行断言
        self.assertIn('true', r.text.lower())
        # print(r.text.lower())
        logging.info(f"case:创建网关设备关联-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()
