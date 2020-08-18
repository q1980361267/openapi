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

import global_environment

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
            'platform': '1'
        }
        self.signatureNonce = int(time.time())

    def tearDown(self):
        pass

    def test_00(self):  # 执行逻辑::设置入参，参数正确填写
        """新增物模板草稿-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('dmp_productId')

        _url = self.url + '/products/{}/properties/draft'.format(id_pro)
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            "name": "name_" + ''.join(random.sample("12345abcde", 5)),
            "identifier": "identifier_" + ''.join(random.sample("12345abcde", 5)),
            "accessMode": 2,
            "type": 6,
            "unit": "t",
            "minimum": 10.1,
            "maximum": 20.2,
            "class": 1,
            "special": {
                "step": 10.1,
            }
        }

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        result = r.json()
        id = result.get('data').get('id')
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:新增物模板草稿 -成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

        with open(assist_file, 'a') as f:
            _data = {
                "draft_id": id
            }
            yaml.dump(_data, f)

    def test_01(self):  # 执行逻辑::设置入参，参数正确填写
        """根据产品ID查询所有物模板草稿 -成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('dmp_productId')
        _url = self.url + '/products/{}/properties/draft'.format(id_pro)
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
        result = r.json()
        id = result.get('data')[0].get('id')
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:根据产品ID查询所有物模板草稿 -成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

        with open(assist_file, 'a') as f:
            _data = {
                "draft_property_id": id
            }
            yaml.dump(_data, f)

    def test_02(self):  # 执行逻辑::设置入参，参数正确填写
        """更新物模板草稿 -成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('dmp_productId')
            id_property = data.get('draft_property_id')
        _url = self.url + '/products/{}/properties/draft/{}'.format(id_pro, id_property)
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
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:更新物模板草稿 -成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_03(self):  # 执行逻辑::设置入参，参数正确填写
        """发布物模板草稿-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('dmp_productId')

        _url = self.url + '/products/{}/properties/draft/publish'.format(id_pro)
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:发布物模板草稿-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_04(self):  # 执行逻辑::设置入参，参数正确填写
        """根据产品ID查询所有功能-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('dmp_productId')

        _url = self.url + '/products/{}/properties'.format(id_pro)
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
        result = r.json()
        try:
            id = result.get('data')[0].get('id')
            identifier = result.get('data')[0].get('identifier')
            with open(assist_file, 'a') as f:
                _data = {
                    "property_id": id,
                    'identifier_name': identifier
                }
                yaml.dump(_data, f)
        except Exception:
            pass

        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())
        logging.info(
            f"case:根据产品ID查询所有功能-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")



    def test_05(self):  # 执行逻辑::设置入参，参数正确填写
        """根据功能ID查询功能-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('dmp_productId')
            id_property = data.get('property_id')

        _url = self.url + '/products/{}/properties/{}'.format(id_pro, id_property)
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
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:根据功能ID查询功能-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_06(self):  # 执行逻辑::设置入参，参数正确填写
        """根据功能ID查询物模板草稿-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('dmp_productId')
            id_property = data.get('draft_property_id')

        _url = self.url + '/products/{}/properties/draft/{}'.format(id_pro, id_property)
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
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:根据功能ID查询物模板草稿-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()
