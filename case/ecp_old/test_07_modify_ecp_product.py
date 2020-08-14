from urllib import parse
import unittest
import time
import requests
import logging
import urllib3
import json

import yaml

from assist import getSignature

with open("../../zhaoshang_pro_config.json", 'r') as f:
    f_json = json.load(f)
    url = f_json.get("baseURL")
    accessKeyId = f_json.get("accessKeyId")
    accessSecret = f_json.get("secret")

with open('../../assist_config.yaml', 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    id_pro = data.get('ecp_productId')


class Test_modifyNodeDevFeature(unittest.TestCase):
    """修改边缘终端产品(mqtt)接口"""

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
        self.url = url + '/products' + '/' + str(self.id_pro)
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
        """修改边缘终端产品(mqtt)-成功"""

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.put(url=self.url, params=params, data=json.dumps(body), headers=self.headers)
        # success = r.json()['success']
        # 断言success字段中的值
        self.assertIn('true', r.text.lower())
        # print(r.text.lower())
        logging.info(f"case:修改边缘终端产品(mqtt)-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n"
                     f"请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()
