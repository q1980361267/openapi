from urllib import parse
import unittest
import time
import requests
import logging
import urllib3
import json
import json

from assist import getSignature

with open('zhaoshang_pro_config.json', 'r') as f:
    f_json = json.load(f)
    url = f_json.get("baseURL")
    accessKeyId = f_json.get("accessKeyId")
    accessSecret = f_json.get("secret")


class Test_CreateNodeProduct(unittest.TestCase):
    """创建网关产接口"""


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
        self.url = url + '/products/mqtt'
        self.accessKey = accessKeyId
        self.accessKeySecret = accessSecret
        self.headers = {
            'Content-Type': 'application/json',
            'platform': '2'
        }

        self.signatureNonce = int(time.time() * 1000)

    def tearDown(self):
        pass

    def test_00(self):  # 执行逻辑::设置入参，参数正确填写
        """创建网关产品-成功"""
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            'name': 'edge_node_product_' + str(int(time.time()))

        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        # print(signature)
        r = requests.post(url=self.url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        self.assertIn('true', r.text)
        logging.info(f"case:创建网关产品-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头："
                     f"{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()
