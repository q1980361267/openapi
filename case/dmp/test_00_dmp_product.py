from urllib import parse
import unittest
import time
import requests
import logging
import urllib3
import json
import json
import yaml
import random
from assist import getSignature
import global_environment

config_file = global_environment.configFilePath()
assist_file = global_environment.assistFilePath()

with open(config_file, 'r') as f:
    f_json = json.load(f)
    url = f_json.get("baseURL")
    accessKeyId = f_json.get("accessKeyId")
    accessSecret = f_json.get("secret")


class Test_DmpProduct(unittest.TestCase):
    """产品接口"""

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

        self.signatureNonce = int(time.time() * 1000)

    def tearDown(self):
        pass

    def test_00(self):  # 执行逻辑::设置入参，参数正确填写, 入参有很多，这里选中mqtt自定义协议产品
        """创建产品-成功"""
        _url = self.url + '/products'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            "authenticationMethod": 1,
            "dataFormat": 2,
            "model": 1,
            "name": "product_" + ''.join(random.sample('12345abcde', 5)),
            "nodeType": 1,
            "protocolType": 1,
            "networkMethod": 1
        }

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        # print(signature)
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        result = r.json()

        id = result.get('data').get('id')
        masterKey = result.get('data').get('masterKey')
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text)

        logging.info(f"case:创建产品-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头："
                     f"{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

        with open(assist_file, 'a') as f:
            _data = {
                "dmp_productId": id,
                "dmp_productSecret": masterKey
            }
            yaml.dump(_data, f)

    def test_01(self):  # 执行逻辑::设置入参，参数正确填写
        """根据产品ID查询产品信息-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('dmp_productId')

        _url = self.url + '/products/{}'.format(id_pro)

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)

        print(r.url)
        print(r.json())
        # success = r.json()['success']
        # print(self.signatureNonce)
        # 断言success字段中的值
        self.assertIn('true', r.text.lower())
        logging.info(
            f"case:根据产品ID查询产品信息-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_02(self):  # 执行逻辑::设置入参，参数正确填写
        """查询产品列表信息-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('ecp_node_deviceId')

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

        print(r.url)
        print(r.json())
        # success = r.json()['success']
        # print(self.signatureNonce)
        # 断言success字段中的值
        self.assertIn('true', r.text.lower())
        logging.info(
            f"case:查询产品列表信息-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_03(self):  # 执行逻辑::设置入参，参数正确填写
        """更改产品-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('dmp_productId')

        _url = self.url + '/products/{}'.format(id_pro)

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'PUT')
        params['signature'] = signature
        r = requests.put(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)

        print(r.url)
        print(r.json())
        # success = r.json()['success']
        # print(self.signatureNonce)
        # 断言success字段中的值
        self.assertIn('true', r.text.lower())
        logging.info(
            f"case:更改产品-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")



if __name__ == '__main__':
    unittest.main()
