from urllib import parse
import unittest
import time
import requests
import logging
import urllib3
import json
import yaml
import random
from assist import getSignature

with open("../../zhaoshang_pro_config.json", 'r') as f:
    f_json = json.load(f)
    url = f_json.get("baseURL")
    accessKeyId = f_json.get("accessKeyId")
    accessSecret = f_json.get("secret")

with open('../../assist_config.yaml', 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    id_enPro = data.get('ecp_node_productId')


class Test_createNodeDevice(unittest.TestCase):
    """创建网关设备接口"""

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
        self.url = url + '/devices/gateway'
        self.accessKey = accessKeyId
        self.accessKeySecret = accessSecret
        self.headers = {
            'Content-Type': 'application/json',
            'platform': '2'
        }
        self.signatureNonce = int(time.time())
        self.id_enPro = id_enPro

    def tearDown(self):
        pass

    def test_00(self):  # 执行逻辑::设置入参，参数正确填写
        """创建网关设备-成功"""

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'productId': self.id_enPro
        }
        body = {
            'name': 'edge_node_dev' + ''.join(random.sample('abcdefghijk0123456', 5)) ,
            'cpuType': 0,
            'systemType': 0
        }

        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=self.url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        result = r.json()
        id = result.get('data').get('id')
        apiKey = result.get('data').get('apiKey')
        # print(result)
        # success = r.json()['success']
        # print(self.signatureNonce)
        # 断言success字段中的值
        self.assertIn('true', r.text.lower())
        logging.info(
            f"case:创建网关设备-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

        with open('../../assist_config.yaml', 'a+') as f:
            _data = {
                "ecp_node_deviceId": id,
                "ecp_node_deviceSecret": apiKey
            }
            yaml.dump(_data, f)


    # def test_01(self):  # 执行逻辑::设置入参，参数正确填写
    #     """异常状态1-名称过长"""
    #
    #     params = {
    #         'accessKeyId': self.accessKey,
    #         'signatureNonce': self.signatureNonce,
    #         'productId': self.id_enPro
    #     }
    #     body = {
    #         'name': 'edge_node_dev01',
    #         'cpuType': 0,
    #         'systemType': 0
    #     }
    #
    #     signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
    #     params['signature'] = signature
    #     r = requests.post(url=self.url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
    #     # success = r.json()['success']
    #     # print(self.signatureNonce)
    #     # 断言success字段中的值
    #     self.assertIn('false', r.text.lower())
    #     logging.info(
    #         f"case:创建网关设备-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()
