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





class Test_FunctionModel(unittest.TestCase):
    """物模型接口"""

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

    def test_00(self):  # 执行逻辑::设置入参，参数正确填写
        """分页查询BACnet属性（bacnet）-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('ecp_productId')

        _url = self.url + '/products/protocol/7/property/page'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'productId': id_pro,
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
            f"case:分页查询BACnet属性（modbus）-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_01(self):  # 执行逻辑::设置入参，参数正确填写
        """创建BACnet物模型草稿（bacnet）-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('ecp_productId')

        _url = self.url + '/products/protocol/7/property/draft'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            "productId": id_pro,
            "name": "name_" + ''.join(random.sample('123450abcdef', 5)),
            "identifier": "identifier_" + ''.join(random.sample('123450abcdef', 5)),
            "type": 1,
            "unit": "1",
            "special": {
                "length": 1
            },
            "accessMode": 2,
            "class": 1,
            "kind": 2,
            "propertyId": 85,
            "objectType": 0,
            "objectId": "1"
        }

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        result = r.json()
        id_property = result.get('data').get('propertyId')
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:分页查询BACnet属性（modbus）-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


    def test_02(self):  # 执行逻辑::设置入参，参数正确填写
        """根据BACnet产品ID查询物模型草稿（bacnet）-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('ecp_productId')

        _url = self.url + '/products/protocol/7/property/draft'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'productId': id_pro
        }
        body = {}

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        result = r.json()
        id = result.get('data')[0].get('id')
        name = result.get('data')[0].get('identifier')
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:根据BACnet产品ID查询物模型草稿-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

        with open(assist_file, 'a') as f:
            _data = {
                "draft_property_id": id
            }
            yaml.dump(_data, f)

    def test_03(self):  # 执行逻辑::设置入参，参数正确填写
        """更新BACnet物模草稿（bacnet）-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id = data.get('draft_property_id')
            id_pro = data.get('ecp_productId')

        _url = self.url + '/products/protocol/7/property/draft'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'productId': id_pro
        }
        body = {
            'id': id,
            "productId": id_pro,
            "name": "name_" + ''.join(random.sample('123450abcdef', 5)),
            "identifier": "identifier_" + ''.join(random.sample('123450abcdef', 5)),
            "type": 1,
            "unit": "1",
            "special": {
                "length": 1
            },
            "accessMode": 2,
            "class": 1,
            "kind": 2,
            "propertyId": 85,
            "objectType": 0,
            "objectId": "1"
        }

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'PUT')
        params['signature'] = signature
        r = requests.put(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值

        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:更新BACnet物模草稿-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


    def test_04(self):  # 执行逻辑::设置入参，参数正确填写
        """根据BACnet产品ID发布物模型草稿（bacnet）-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('ecp_productId')

        _url = self.url + '/products/protocol/7/property/draft/publish/{}'.format(id_pro)
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'productId': id_pro
        }
        body = {}

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值

        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:根据BACnet产品ID发布物模型草稿-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_05(self):  # 执行逻辑::设置入参，参数正确填写
        """分页查询BACnet物模型草稿（bacnet）-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('ecp_productId')

        _url = self.url + '/products/protocol/7/property/draft/page'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'productId': id_pro,
            'pageSize': 10,
            'currentPage': 1
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
            f"case:分页查询BACnet物模型草稿-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


    def test_06(self):  # 执行逻辑::设置入参，参数正确填写
        """根据BACnet产品ID查询所有功能（bacnet）-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('ecp_productId')

        _url = self.url + '/products/protocol/7/property'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'productId': id_pro
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        result = r.json()
        id = result.get('data')[0].get('id')
        identifier = result.get('data')[0].get('identifier')
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:创建边缘终端功能草稿（modbus）-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

        with open(assist_file, 'a') as f:
            _data = {
                "property_id": id,
                "identifier_name": identifier
            }
            yaml.dump(_data, f)

    def test_07(self):  # 执行逻辑::设置入参，参数正确填写
        """根据BACnet属性ID查询BACnet属性信息（bacnet）-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id = data.get('property_id')

        _url = self.url + '/products/protocol/7/property/{}'.format(id)
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
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
            f"case:根据BACnet属性ID查询BACnet属性信息-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_08(self):  # 执行逻辑::设置入参，参数正确填写
        """根据BACnet属性ID查询BACnet物模型草稿-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id = data.get('draft_property_id')

        _url = self.url + '/products/protocol/7/property/draft/{}'.format(id)
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
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
            f"case:根据BACnet属性ID查询BACnet属性信息-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    # def test_09(self):  # 执行逻辑::设置入参，参数正确填写
    #     """根据BACnet属性ID删除BACnet属性-成功"""
    #     with open(assist_file, 'r') as f:
    #         data = yaml.load(f, Loader=yaml.FullLoader)
    #         id = data.get('property_id')
    #
    #     _url = self.url + '/products/protocol/7/property/{}'.format(id)
    #     params = {
    #         'accessKeyId': self.accessKey,
    #         'signatureNonce': self.signatureNonce
    #     }
    #     body = {}
    #
    #     signature = getSignature.get_signature(params, body, self.accessKeySecret, 'DELETE')
    #     params['signature'] = signature
    #     r = requests.delete(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
    #     # success = r.json()['success']
    #     # 断言success字段中的值
    #
    #     print(_url)
    #     print(r.json())
    #     self.assertIn('true', r.text.lower())
    #
    #     logging.info(
    #         f"case:根据BACnet属性ID删除BACnet属性-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
    #         f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")
    #


if __name__ == '__main__':
    unittest.main()
