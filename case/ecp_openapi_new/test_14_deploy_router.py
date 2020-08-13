# coding:gbk
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


# with open(assist_file, 'r') as f:
#     data = yaml.load(f, Loader=yaml.FullLoader)
#     id_gateway = data.get('ecp_node_deviceId')
#     id_dev = data.get('ecp_deviceId')
#     id_pro = data.get('ecp_productId')

class Test_Router(unittest.TestCase):
    """数据路由接口"""

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
        """分配路由实例至某边缘节点-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('ecp_node_deviceId')
            id_router = data.get('edge_router_id')

        _url = self.url + '/routers/gateway/association'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            'devId': str(id_dev),
            'exportClientId': [id_router]
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:分配路由实例至某边缘节点-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_01(self):  # 执行逻辑::设置入参，参数正确填写
        """分页查询已分配至边缘节点的路由实例-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('ecp_node_deviceId')

        _url = url + '/routers/gateway/association'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'currentPage': 1,
            'pageSize': 10,
            'deviceId': id_dev
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:分页查询已分配至边缘节点的路由实例-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_03(self):  # 执行逻辑::设置入参，参数正确填写
        """分页查询未分配的路由实例信息-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('ecp_node_deviceId')

        _url = url + '/routers/gateway/unassignedclient'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'currentPage': 1,
            'pageSize': 10,
            'deviceId': id_dev
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:分页查询未分配的路由实例信息-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()
