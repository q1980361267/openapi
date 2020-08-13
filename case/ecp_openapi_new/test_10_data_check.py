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

class Test_Lable(unittest.TestCase):
    """查询标签接口"""

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
            'platform': '3'
        }
        self.signatureNonce = int(time.time())

    def tearDown(self):
        pass

    def test_00(self):  # 执行逻辑::设置入参，参数正确填写
        """查询设备的多个属性值的最新值-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('ecp_deviceId')
            identifier = data.get('identifier_name')

        _url = url + '/data/properties/recent/value'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'deviceId': id_dev,
            'propertyNames': identifier
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

        logging.info(f"case:查询标签-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


    def test_01(self):  # 执行逻辑::设置入参，参数正确填写
        """分页查询资源某时间段数据点-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('ecp_deviceId')

        _url = url + '/data/device/{}'.format(id_dev)
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'start': 1596178896813,
            'end': 1596783696813,
            'currentPage': 1,
            'pageSize': 10
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

        logging.info(f"case:查询标签-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()
