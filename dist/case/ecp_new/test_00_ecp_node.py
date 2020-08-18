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


class Test_CreateNodeProduct(unittest.TestCase):
    """边缘节点接口"""

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

        self.signatureNonce = int(time.time() * 1000)

    def tearDown(self):
        pass

    def test_00(self):  # 执行逻辑::设置入参，参数正确填写
        """创建节点-成功"""
        _url = self.url + '/edgenode/pro'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            'name': 'edge_node_' + ''.join(random.sample('0123456abcdef', 5)),
            "cpuType": 2,
            "systemType": 0
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        # print(signature)
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        try:
            result = r.json()

            id = result.get('data').get('id')
            masterKey = result.get('data').get('apiKey')
            with open(assist_file, 'a') as f:
                _data = {
                    "ecp_node_deviceId": id,
                    "ecp_node_deviceSecret": masterKey
                }
                yaml.dump(_data, f)
        except Exception:
            pass

        print(_url)
        print(r.json())
        self.assertIn('true', r.text)

        logging.info(f"case:创建网关产品-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头："
                     f"{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_01(self):  # 执行逻辑::设置入参，参数正确填写
        """查看边缘节点属性-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('ecp_node_deviceId')

        _url = self.url + '/edgenode/pro/' + str(id_dev)

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)

        print(_url)
        print(r.json())
        # success = r.json()['success']
        # print(self.signatureNonce)
        # 断言success字段中的值
        self.assertIn('true', r.text.lower())
        logging.info(
            f"case:查看边缘节点属性-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_02(self):  # 执行逻辑::设置入参，参数正确填写
        """更新边缘节点属性-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('ecp_node_deviceId')

        _url = self.url + '/edgenode/pro/' + str(id_dev)

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'put')
        params['signature'] = signature
        r = requests.put(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)

        print(_url)
        print(r.json())
        # success = r.json()['success']
        # print(self.signatureNonce)
        # 断言success字段中的值
        self.assertIn('true', r.text.lower())
        logging.info(
            f"case:更新边缘节点属性-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_03(self):  # 执行逻辑::设置入参，参数正确填写
        """分页查询边缘节点属性-成功"""

        _url = self.url + '/edgenode/pro/page'

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

        print(_url)
        print(r.json())
        # success = r.json()['success']
        # print(self.signatureNonce)
        # 断言success字段中的值
        self.assertIn('true', r.text.lower())
        logging.info(
            f"case:分页查询边缘节点属性-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_04(self):  # 执行逻辑::设置入参，参数正确填写
        """查询边缘节点配置信息-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('ecp_node_deviceId')

        _url = self.url + '/devices/gateway/information/' + str(id_dev)

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)

        print(_url)
        print(r.json())
        # success = r.json()['success']
        # print(self.signatureNonce)
        # 断言success字段中的值
        self.assertIn('true', r.text.lower())
        logging.info(
            f"case:查询边缘节点配置信息-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_05(self):  # 执行逻辑::设置入参，参数正确填写,protocol参数选择为7（1、4、5、7可选择）
        """查询边缘节点下所有关联的边缘终端-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('ecp_node_deviceId')

        _url = self.url + '/devices/gateway/multi/' + str(id_dev) + '/7'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)

        print(_url)
        print(r.json())
        # success = r.json()['success']
        # print(self.signatureNonce)
        # 断言success字段中的值
        self.assertIn('true', r.text.lower())
        logging.info(
            f"case:查询边缘节点配置信息-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_06(self):  # 执行逻辑::设置入参，参数正确填写
        """批量禁用边缘节点节点-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('ecp_node_deviceId')

        _url = self.url + '/edgenode/pro/adminstate/multi'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'id': str(id_dev),
            'adminState': 0
        }
        body = {}

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'PUT')
        params['signature'] = signature
        r = requests.put(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)

        print(_url)
        print(r.json())
        # success = r.json()['success']
        # print(self.signatureNonce)
        # 断言success字段中的值
        self.assertIn('true', r.text.lower())
        logging.info(
            f"case:批量禁用边缘节点节点-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_07(self):  # 执行逻辑::设置入参，参数正确填写
        """批量启用边缘节点-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('ecp_node_deviceId')

        _url = self.url + '/edgenode/pro/adminstate/multi'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'id': str(id_dev),
            'adminState': 1
        }
        body = {}

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'PUT')
        params['signature'] = signature
        r = requests.put(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)

        print(_url)
        print(r.json())
        # success = r.json()['success']
        # print(self.signatureNonce)
        # 断言success字段中的值
        self.assertIn('true', r.text.lower())
        logging.info(
            f"case:批量启用边缘节点-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_08(self):  # 执行逻辑::设置入参，参数正确填写
        """查询边缘节点的功能列表-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('ecp_node_deviceId')

        _url = self.url + '/edgenode/pro/properties'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)

        print(_url)
        print(r.json())
        # success = r.json()['success']
        # print(self.signatureNonce)
        # 断言success字段中的值
        self.assertIn('true', r.text.lower())
        logging.info(
            f"case:查询边缘节点的功能列表-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()
