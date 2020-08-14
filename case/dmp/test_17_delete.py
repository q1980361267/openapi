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

class Test_Delete(unittest.TestCase):
    """删除+解除分配接口"""

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
            'platform': '1'
        }
        self.signatureNonce = int(time.time())

    def tearDown(self):
        pass

    def test_01(self):  # 执行逻辑::设置入参，参数正确填写
        """删除物模板草稿属性-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('dmp_productId')
            id_draft = data.get('draft_property_id')

        _url = self.url + '/products/{}/properties/draft/{}'.format(id_pro, id_draft)
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'DELETE')
        params['signature'] = signature
        r = requests.delete(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值

        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:删除物模板草稿-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_02(self):  # 执行逻辑::设置入参，参数正确填写
        """删除邮箱服务器-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_mail = data.get('mail_id')

        _url = self.url + '/mail/server/id/{}'.format(id_mail)

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'DELETE')
        params['signature'] = signature
        r = requests.delete(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:删除邮箱服务器-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_03(self):  # 执行逻辑::设置入参，参数正确填写
        """删除邮箱模板-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_template = data.get('template_id')

        _url = self.url + '/mail/pattern/id/{}'.format(id_template)

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'DELETE')
        params['signature'] = signature
        r = requests.delete(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:删除邮箱模板-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_04(self):  # 执行逻辑::设置入参，参数正确填写
        """通过id删除规则-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_rule = data.get('rule_id')

        _url = self.url + '/rules/{}'.format(id_rule)

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'DELETE')
        params['signature'] = signature
        r = requests.delete(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:通过id删除规则-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_05(self):  # 执行逻辑::设置入参，参数正确填写
        """删除路由实例（云端）-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_router = data.get('router_id')

        _url = self.url + '/routers/{}'.format(id_router)

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'DELETE')
        params['signature'] = signature
        r = requests.delete(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:删除路由实例（云端）-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_06(self):  # 执行逻辑::设置入参，参数正确填写
        """删除路由目的地端点-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_destination = data.get('destination_id')

        _url = self.url + '/address-configs/{}'.format(id_destination)

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'DELETE')
        params['signature'] = signature
        r = requests.delete(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:删除路由目的地端点-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_07(self):  # 执行逻辑::设置入参，参数正确填写
        """批量将多个设备移除分组-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('dmp_deviceId')
            id_group = data.get('group_id')

        _url = self.url + '/label/remove/devices'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            "deviceIds": [
                id_dev
            ],
            "labelId": id_group
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'PUT')
        params['signature'] = signature
        r = requests.put(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:批量将多个设备移除分组-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_08(self):  # 执行逻辑::设置入参，参数正确填写
        """删除分组-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_group = data.get('group_id')

        _url = self.url + '/label'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            'ids': [id_group]
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'DELETE')
        params['signature'] = signature
        r = requests.delete(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:删除分组-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_09(self):  # 执行逻辑::设置入参，参数正确填写
        """删除设备-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('dmp_deviceId')

        _url = self.url + '/devices/{}'.format(id_dev)

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'DELETE')
        params['signature'] = signature
        r = requests.delete(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:删除设备-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_10(self):  # 执行逻辑::设置入参，参数正确填写
        """删除产品-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('dmp_productId')

        _url = self.url + '/products/{}'.format(id_pro)

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'DELETE')
        params['signature'] = signature
        r = requests.delete(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:删除产品-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()
