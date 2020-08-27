# coding:utf-8
from urllib import parse
import unittest
import time
import requests
import logging
import urllib3
import json
import random
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



class Test_EcpProduct(unittest.TestCase):
    """边缘产品接口"""

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
        self.url = url
        self.accessKey = accessKeyId
        self.accessKeySecret = accessSecret
        self.headers = {
            'Content-Type': 'application/json',
            'platform': '3'
        }
        self.signatureNonce = int(time.time())

    def tearDown(self):
        pass

    def test_00(self):  # 执行逻辑::设置入参，参数正确填写, protocol参数选择7，bacnet（1,4,5,7）
        """创建边缘终端产品(BACnet)-成功"""
        _url = self.url + '/products'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
        }
        body = {
            'name': 'bacnet_product_' + "".join(random.sample("abcdefgh0123456", 5)),
            'protocolType': 7,
            'model': 1,
            'dataFormat': 1,
            'nodeType': 1,
            "networkMethod": 1
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        result = r.json()
        try:
            id = result.get('data').get('id')
            masterKey = result.get('data').get('masterKey')
            with open(assist_file, 'a') as f:
                _data = {
                    "ecp_productId": id,
                    "ecp_productSecret": masterKey
                }
                yaml.dump(_data, f)
        except Exception:
            pass
        # success = r.json()['success']
        # 断言success字段中的值
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:创建边缘终端产品(BACnet)-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")



    def test_00_00(self):  # 执行逻辑::设置入参，参数正确填写, protocol参数选择1，mqtt（1,4,5,7）
        """创建边缘终端产品(MQTT)-成功"""
        _url = self.url + '/products'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
        }
        body = {
            'name': 'mqtt_product_' + "".join(random.sample("abcdefgh0123456", 5)),
            'protocolType': 1,
            'model': 1,
            'dataFormat': 1,
            'nodeType': 1,
            "networkMethod": 1
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        result = r.json()
        try:
            id = result.get('data').get('id')
            masterKey = result.get('data').get('masterKey')
            with open(assist_file, 'a') as f:
                _data = {
                    "ecp_productId_mqtt": id,
                    "ecp_productSecret_mqtt": masterKey
                }
                yaml.dump(_data, f)
        # success = r.json()['success']
        # 断言success字段中的值
        except Exception as e:
            pass
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:创建边缘终端产品(mqtt)-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_00_01(self):  # 执行逻辑::设置入参，参数正确填写, protocol:4，dataFormat:3
        """创建边缘终端产品(modbus)-成功"""
        _url = self.url + '/products'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
        }
        body = {
            'name': 'modbus_product_' + "".join(random.sample("abcdefgh0123456", 5)),
            'protocolType': 4,
            'model': 1,
            'dataFormat': 3,
            'nodeType': 1,
            "networkMethod": 1
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        result = r.json()
        try:
            id = result.get('data').get('id')
            masterKey = result.get('data').get('masterKey')
            with open(assist_file, 'a') as f:
                _data = {
                    "ecp_productId_modbus": id,
                    "ecp_productSecret_modbus": masterKey
                }
                yaml.dump(_data, f)
        except Exception:
            pass
        # success = r.json()['success']
        # 断言success字段中的值
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:创建边缘终端产品(modbus)-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_00_02(self):  # 执行逻辑::设置入参，入参改变, protocol:5
        """创建边缘终端产品(opcua)-成功"""
        _url = self.url + '/products'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
        }
        body = {
            'name': 'opcua_product_' + "".join(random.sample("abcdefgh0123456", 5)),
            'protocolType': 5,
            'model': 1,
            'dataFormat': 1,
            'nodeType': 1,
            "networkMethod": 1
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        result = r.json()
        try:
            id = result.get('data').get('id')
            masterKey = result.get('data').get('masterKey')
            with open(assist_file, 'a') as f:
                _data = {
                    "ecp_productId_opcua": id,
                    "ecp_productSecret_opcua": masterKey
                }
                yaml.dump(_data, f)
        except Exception:
            pass
        # success = r.json()['success']
        # 断言success字段中的值
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:创建边缘终端产品(opcua)-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_01(self):  # 执行逻辑::设置入参，参数正确填写, protocol参数选择7，bacnet（1,4,5,7）
        """根据产品ID查询产品信息-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('ecp_productId')

        _url = self.url + '/products/' + str(id_pro)

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:根据产品ID查询产品信息-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_02(self):  # 执行逻辑::设置入参，参数正确填写, protocol参数选择7，bacnet（1,4,5,7）
        """查询产品列表信息-成功"""

        _url = self.url + '/products'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'currentPage': 1,
            'pageSize': 10
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:查询产品列表信息-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_03(self):  # 执行逻辑::设置入参，参数正确填写, protocol参数选择7，bacnet（1,4,5,7）
        """更改产品-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('ecp_productId')

        _url = self.url + '/products/' + str(id_pro)

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'PUT')
        params['signature'] = signature
        r = requests.put(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:更改产品-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()
