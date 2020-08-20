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

class Test_Statistic(unittest.TestCase):
    """查询统计接口"""

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
        """查询查询数据转发最近的聚合数据-成功"""
        _url = url + '/routers/data/last'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'interval': 1,
            'count': 2
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:查询标签-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


    def test_01(self):  # 执行逻辑::设置入参，参数正确填写
        """查询消息路由实例总数-成功"""
        _url = url + '/routers/count'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'platform': 2
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:查询标签-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


    def test_02(self):  # 执行逻辑::设置入参，参数正确填写
        """数据上传数量统计-成功"""
        _url = url + '/data/overview/count/event'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'uploadDuration': 1
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:查询标签-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


    def test_03(self):  # 执行逻辑::设置入参，参数正确填写
        """按时间段统计设备数量-成功"""
        _url = url + '/data/overview/count/duration'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'nodeDeviceDuration': 1
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:按时间段统计设备数量-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_04(self):  # 执行逻辑::设置入参，参数正确填写
        """设备实时数量统计-成功"""
        _url = url + '/data/overview/count/realtime'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:设备实时数量统计-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()
