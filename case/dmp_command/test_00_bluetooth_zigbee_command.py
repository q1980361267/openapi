# coding:utf-8
from urllib import parse
import unittest
import time
import requests
import logging
import urllib3
import json

import yaml

from assist import getSignature

from config import global_environment


config_file = global_environment.configFilePath()
assist_file = global_environment.assistFilePath()


with open(config_file, 'r') as f:
    f_json = json.load(f)
    url = f_json.get("baseURL")
    accessKeyId = f_json.get("accessKeyId")
    accessSecret = f_json.get("secret")


# with open(assist_file, 'r') as f:
#     data = yaml.load(f, Loader=yaml.FullLoader)
#     id_gateway = data.get('ecp_node_deviceId')
#     id_dev = data.get('ecp_deviceId')
#     id_pro = data.get('ecp_productId')

class Test_DataCheck(unittest.TestCase):
    """Bluetooth和Zigbee命令管理接口"""

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
        # self.id_pro = id_pro
        # self.id_gateway = "10082804"

        self.accessKey = accessKeyId
        self.accessKeySecret = accessSecret
        self.headers = {
            'Content-Type': 'application/json',
            'platform': '1'
        }
        self.signatureNonce = int(time.time())

    def tearDown(self):
        pass

    def test_00(self):  # 执行逻辑::设置入参，参数正确填写
        """通过deviceId异步下发读取命令（bluetooth）-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('dmp_deviceId')
            identifier = data.get('identifier_name')

        _url = url + '/commands-async/lightweight'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            "deviceId": 10005881,
            "functionType": "propertyGet",
            "identifier": "key",
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:通过deviceId异步下发读取命令（bluetooth）-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_01(self):  # 执行逻辑::设置入参，参数正确填写
        """通过deviceId异步下发写命令（bluetooth）-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('dmp_deviceId')
            identifier = data.get('identifier_name')

        _url = url + '/commands-async/lightweight'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            "deviceId": 10005881,
            "functionType": "propertySet",
            "identifier": "key",
            "identifierValue": 88
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:通过deviceId异步下发写命令（bluetooth）-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_02(self):  # 执行逻辑::设置入参，参数正确填写
        """通过productId + deviceName异步下发读命令（bluetooth）-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('dmp_deviceId')
            identifier = data.get('identifier_name')

        _url = url + '/command/byname/async'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            "productId": 100650,
            "deviceName": "subdev-one-19",
            "functionType": "propertyGet",
            "identifier": "key"
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:通过productId + deviceName异步下发读命令（bluetooth）-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_03(self):  # 执行逻辑::设置入参，参数正确填写
        """通过productId + deviceName异步下发写命令（bluetooth）-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('dmp_deviceId')
            identifier = data.get('identifier_name')

        _url = url + '/command/byname/async'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            "productId": 100650,
            "deviceName": "subdev-one-19",
            "functionType": "propertySet",
            "identifier": "key",
            "identifierValue": 99
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:通过productId + deviceName异步下发写命令（bluetooth）-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_04(self):  # 执行逻辑::设置入参，参数正确填写
        """分组批量下发异步读命令（bluetooth）-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('dmp_deviceId')
            identifier = data.get('identifier_name')

        _url = url + '/command/multi/lightweight'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            "groupId": 413,
            "functionType": "propertyGet",
            "identifier": "key"
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:分组批量下发异步读命令（bluetooth）-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_05(self):  # 执行逻辑::设置入参，参数正确填写
        """分组批量下发异步写命令（bluetooth）-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('dmp_deviceId')
            identifier = data.get('identifier_name')

        _url = url + '/command/multi/lightweight'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            "groupId": 413,
            "functionType": "propertySet",
            "identifier": "key",
            "identifierValue": 123
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:分组批量下发异步写命令（bluetooth）-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()