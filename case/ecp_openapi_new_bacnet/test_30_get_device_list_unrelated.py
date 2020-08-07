# coding:gbk
from urllib import parse
import unittest
import time
import requests
import logging
import urllib3
import json

import yaml

from assist import getSignature

with open("../../test_config.json", 'r') as f:
    f_json = json.load(f)
    url = f_json.get("baseURL")
    accessKeyId = f_json.get("accessKeyId")
    accessSecret = f_json.get("secret")

with open('../../assist_config.yaml', 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    id_gateway = data.get('ecp_node_deviceId')
    id_dev = data.get('ecp_deviceId')
    id_pro = data.get('ecp_productId')

class Test_CreateGatewayDeviceAssociate(unittest.TestCase):
    """分页查询边缘节点关联的边缘终端（NIN）接口"""

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
        self.id_pro = id_pro
        self.id_gateway = "10082804"
        self.url = url + '/devices/subdevice/NIN/page'
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
        """分页查询边缘节点关联的边缘终端（NIN）-成功"""
        params = {
            'accessKeyId': self.accessKey,
            'currentPage': 1,
            'parentId': self.id_gateway,
            'pageSize': 10,
            'protocol': 7,
            'product': self.id_pro,
            'signatureNonce': self.signatureNonce
        }
        body = {

        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=self.url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 对响应的结果进行断言
        print(r.json())
        print(self.url)
        print(params)
        self.assertIn('true', r.text.lower())

        logging.info(f"case:分页查询边缘节点关联的边缘终端（NIN）-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()
