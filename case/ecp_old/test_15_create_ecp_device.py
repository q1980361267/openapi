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

with open("../../zhaoshang_pro_config.json", 'r') as f:
    f_json = json.load(f)
    url = f_json.get("baseURL")
    accessKeyId = f_json.get("accessKeyId")
    accessSecret = f_json.get("secret")

with open('../../assist_config.yaml', 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    pro_id = data.get('ecp_productId')


class Test_ModifyEdgeTerminalDevice(unittest.TestCase):
    """创建边缘终端设备(modbus)接口"""

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
        self.id_pro = pro_id
        self.url = url + '/devices'
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
        """创建边缘终端设备(modbus)-成功"""

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'productId': self.id_pro
        }
        body = {
            "name": "modbus_dev_" + ''.join(random.sample('1234567890abcdefghijklmn', 5)),
            "description": "这是一个modbus终端设备"
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=self.url, params=params, data=json.dumps(body), headers=self.headers)
        # success = r.json()['success']
        # 对响应的结果进行断言
        result = r.json()
        id = result.get('data').get('id')
        secret = result.get('data').get('apiKey')
        # print(r.json())
        self.assertIn('true', r.text.lower())
        # print(r.text.lower())
        logging.info(f"case:创建边缘终端设备(modbus)-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

        with open('../../assist_config.yaml', 'a') as f:
            _data = {
                "ecp_deviceId": id,
                "ecp_deviceSecrete": secret
            }
            yaml.dump(_data, f)


if __name__ == '__main__':
    unittest.main()
