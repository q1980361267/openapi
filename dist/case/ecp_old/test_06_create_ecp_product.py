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

with open("../../zhaoshang_test_config.json", 'r') as f:
    f_json = json.load(f)
    url = f_json.get("baseURL")
    accessKeyId = f_json.get("accessKeyId")
    accessSecret = f_json.get("secret")


class Test_modifyNodeDevFeature(unittest.TestCase):
    """创建边缘终端产品(mqtt)接口"""

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
        self.url = url + '/products'
        self.accessKey = accessKeyId
        self.accessKeySecret = accessSecret
        self.headers = {
            'Content-Type': 'application/json',
            'platform': '2'
        }
        self.signatureNonce = int(time.time())

    def tearDown(self):
        pass

    def test_00(self):  # 执行逻辑::设置入参，参数正确填写
        """创建边缘终端产品(mqtt)-成功"""

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
        }
        body = {
            'name': 'edge_terminal_product_' + "".join(random.sample("abcdefgh0123456", 5)),
            'protocolType': 4,
            'model': 1,
            'dataFormat': 3,
            'nodeType': 1,
            "networkMethod": 1
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=self.url, params=params, data=json.dumps(body), headers=self.headers)
        result = r.json()
        id = result.get('data').get('id')
        masterKey = result.get('data').get('masterKey')
        # success = r.json()['success']
        # 断言success字段中的值
        # print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(
            f"case:创建边缘终端产品(mqtt)-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
            f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

        with open('../../assist_config.yaml', 'a') as f:
            _data = {
                "ecp_productId": id,
                "ecp_productSecret": masterKey
            }
            yaml.dump(_data, f)


if __name__ == '__main__':
    unittest.main()
