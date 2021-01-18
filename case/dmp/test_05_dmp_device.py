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
from assist.getProjectId import get_projectId

config_file = global_environment.configFilePath()
assist_file = global_environment.assistFilePath()

with open(config_file, 'r') as f:
    f_json = json.load(f)
    url = f_json.get("baseURL")
    accessKeyId = f_json.get("accessKeyId")
    accessSecret = f_json.get("secret")
    projectId = get_projectId(accessKeyId, accessSecret)


class Test_DmpDevice(unittest.TestCase):
    """设备接口"""

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
            'platform': '1',
            'projectId': projectId
        }
        self.signatureNonce = int(time.time())

    def tearDown(self):
        pass

    def test_00(self):  # 执行逻辑::设置入参，参数正确填写
        """注册设备-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('dmp_productId')

        _url = self.url + '/devices'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'productId': id_pro
        }
        body = {
            'name': 'dev_' + ''.join(random.sample('012345abcde', 5))
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        try:

            result = r.json()
            id = result.get('data').get('id')
            secret = result.get('data').get('apiKey')
            with open(assist_file, 'a') as f:
                _data = {
                    "dmp_deviceId": id,
                    "dmp_deviceSecret": secret
                }
                yaml.dump(_data, f)
        except Exception:
            print(r.text)

        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())
        logging.info(
            f"case:注册设备-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_00_00(self):  # 执行逻辑::设置入参，参数正确填写
        """注册设备(gateway)-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('dmp_productId_gateway')

        _url = self.url + '/devices'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'productId': id_pro
        }
        body = {
            'name': 'dev_' + ''.join(random.sample('012345abcde', 5))
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        result = r.json()
        id = result.get('data').get('id')
        secret = result.get('data').get('apiKey')

        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:注册设备(gateway)-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

        with open(assist_file, 'a') as f:
            _data = {
                "dmp_deviceId_gateway": id,
                "dmp_deviceSecret_gateway": secret
            }
            yaml.dump(_data, f)

    def test_00_01(self):  # 执行逻辑::设置入参，参数正确填写
        """注册设备(bluetooth)-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('dmp_productId_bluetooth')

        _url = self.url + '/devices'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'productId': id_pro
        }
        body = {
            'name': 'dev_' + ''.join(random.sample('012345abcde', 5))
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        result = r.json()
        id = result.get('data').get('id')
        secret = result.get('data').get('apiKey')

        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:注册设备(gateway)-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

        with open(assist_file, 'a') as f:
            _data = {
                "dmp_deviceId_bluetooth": id,
                "dmp_deviceSecret_bluetooth": secret
            }
            yaml.dump(_data, f)

    def test_01(self):  # 执行逻辑::设置入参，参数正确填写
        """获取设备详情-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('dmp_deviceId')

        _url = self.url + '/devices/{}'.format(id_dev)

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
            f"case:获取设备详情-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_02(self):  # 执行逻辑::设置入参，参数正确填写
        """更新设备的基本属性-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('dmp_deviceId')

        _url = self.url + '/devices/{}'.format(id_dev)

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
            f"case:更新设备的基本属性-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_03(self):  # 执行逻辑::设置入参，参数正确填写
        """按条件分页查询设备-成功"""

        _url = self.url + '/devices/multi'

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
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:更新设备的基本属性-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_04(self):  # 执行逻辑::设置入参，参数正确填写
        """批量创建设备-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('dmp_productId')

        _url = self.url + '/devices/multi'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'productId': id_pro
        }
        body = {"list": [
            {
                "name": "api_device_" + ''.join(random.sample('12345abcde', 5))
            },
            {
                "name": "api_device_" + ''.join(random.sample('12345abcde', 5))
            }
        ]}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:批量创建设备-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_05(self):  # 执行逻辑::设置入参，参数正确填写
        """批量禁用设备-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('dmp_deviceId')

        _url = self.url + '/devices/lock'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            'deviceIds': [id_dev]
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
            f"case:批量禁用设备-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_06(self):  # 执行逻辑::设置入参，参数正确填写
        """批量启用设备-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('dmp_deviceId')

        _url = self.url + '/devices/unlock'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            'deviceIds': [id_dev]
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
            f"case:批量启用设备-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_07(self):  # 执行逻辑::设置入参，参数正确填写
        """分页获取批次列表-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_pro = data.get('dmp_productId')

        _url = self.url + '/products/batch/page'

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
        result = r.json()
        id_batch = result.get('data').get('content')[0].get('id')
        print(r.url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:分页获取批次列表-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

        with open(assist_file, 'a') as f:
            _data = {
                "batch_id": id_batch
            }
            yaml.dump(_data, f)

    def test_08(self):  # 执行逻辑::设置入参，参数正确填写
        """分页获取批次下的设备列表-成功"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_batch = data.get('batch_id')

        _url = self.url + '/devices/batch/page'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'batchId': id_batch,
            'currentPage': 1,
            'pageSize': 10
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
            f"case:分页获取批次下的设备列表-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()
