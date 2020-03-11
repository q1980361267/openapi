# coding:gbk
from urllib import parse
import unittest
import time
import requests
import logging
import urllib3
import json

from lib import getOpenApiPramsTemplate, getSignature, getDeviceInfo


class Test_CreateGatewayDeviceAssociate(unittest.TestCase):
    """批量启用设备接口"""

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
        self.id_dev_first = getDeviceInfo.getGatewayDevicesId()
        self.id_dev_second = getDeviceInfo.getGatewayDevicesIdSecond()
        self.url = getOpenApiPramsTemplate.get_url() + '/devices/unlock'
        self.accessKey = getOpenApiPramsTemplate.getAccesskey()
        self.accessKeySecret = getOpenApiPramsTemplate.getAccessKeySecret()
        self.headers = getOpenApiPramsTemplate.getHeaders()
        self.signatureNonce = int(time.time())

    def tearDown(self):
        pass

    def test_00(self):  # 执行逻辑::设置入参，参数正确填写
        """批量启用设备-成功"""
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            'deviceIds': [self.id_dev_first,self.id_dev_second]
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'PUT')
        params['signature'] = signature
        r = requests.put(url=self.url, params=params, data=json.dumps(body), headers=self.headers)
        # success = r.json()['success']
        # 对响应的结果进行断言
        self.assertIn('true', r.text.lower())
        # print(r.text.lower())
        logging.info(f"case:批量启用设备-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()
