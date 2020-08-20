# coding:utf-8
from urllib import parse
import unittest
import time
import requests
import logging
import urllib3
import json
import json
import yaml

from assist import getSignature

with open('../../test_config.json', 'r') as f:
    f_json = json.load(f)
    url = f_json.get("baseURL")
    accessKeyId = f_json.get("accessKeyId")
    accessSecret = f_json.get("secret")


class Test_CreateNodeProduct(unittest.TestCase):
    """bacnet异步命令接口"""

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
        self.url = url + '/commands/gateway/bacnet/async'
        self.accessKey = accessKeyId
        self.accessKeySecret = accessSecret
        self.headers = {
            'Content-Type': 'application/json',
            'platform': '3'
        }

        self.signatureNonce = int(time.time() * 1000)

    def tearDown(self):
        pass

    def test_00(self):  # 执行逻辑::设置入参，参数正确填写
        """异步读命令（bacnet）-成功"""
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            "deviceId": 10082805,
            "functionType": "propertyGet",
            "identifier": "someFloat"
        }

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        # print(signature)
        r = requests.post(url=self.url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        result = r.json()
        # print(self.url)
        print(result)
        self.assertIn('true', r.text)
        logging.info(f"case:创建网关产品-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头："
                     f"{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


    def test_01(self):  # 执行逻辑::设置入参，参数正确填写
        """异步写命令（bacnet）-成功"""
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            "deviceId": 10082805,
            "functionType": "propertySet",
            "identifier": "someFloat",
            "identifierValue": 66
        }

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        # print(signature)
        r = requests.post(url=self.url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        result = r.json()

        print(result)
        self.assertIn('true', r.text)
        logging.info(f"case:创建网关产品-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头："
                     f"{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


    def test_02(self):  # 执行逻辑::设置入参，参数正确填写
        """异步读命令（bacnet - productID+deviceName）-成功"""
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            "productId": 104191,
            "deviceName": "BACnet设备",
            "functionType": "propertyGet",
            "identifier": "someFloat"

        }
        _url = url + '/command/gateway/async/byname'
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        # print(signature)
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        result = r.json()

        print(result)
        self.assertIn('true', r.text)
        logging.info(f"case:创建网关产品-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头："
                     f"{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_03(self):  # 执行逻辑::设置入参，参数正确填写
        """异步写命令（bacnet-productID+deviceName）-成功"""
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            "productId": 104191,
            "deviceName": "BACnet设备",
            "functionType": "propertySet",
            "identifier": "someFloat",
            "identifierValue": 66

        }
        _url = url + '/command/gateway/async/byname'
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        # print(signature)
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        result = r.json()

        print(result)
        self.assertIn('true', r.text)
        logging.info(f"case:创建网关产品-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头："
                     f"{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_04(self):  # 执行逻辑::设置入参，参数正确填写
        """查询设备最新一条异步命令（bacnet）-成功"""
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}
        _url = url + '/commands-async/10082805/last'
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        # print(signature)
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        result = r.json()

        print(result)
        self.assertIn('true', r.text)
        logging.info(f"case:创建网关产品-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头："
                     f"{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_05(self):  # 执行逻辑::设置入参，参数正确填写
        """查询异步命令详情（bacnet）-成功"""
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}
        _url = url + '/commands-async/' + "3c908a23-1fc3-40d4-8d23-55a7e3117a49"
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        # print(signature)
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        result = r.json()

        print(result)
        self.assertIn('true', r.text)
        logging.info(f"case:创建网关产品-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头："
                     f"{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_06(self):  # 执行逻辑::设置入参，参数正确填写
        """查询异步命令列表（bacnet）-成功"""
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'deviceId': 10082805,
            'pageSize': 10,
            'currentPage': 1
        }
        body = {}
        _url = url + '/commands-async'
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        # print(signature)
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        result = r.json()

        print(result)
        self.assertIn('true', r.text)
        logging.info(f"case:创建网关产品-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头："
                     f"{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()
