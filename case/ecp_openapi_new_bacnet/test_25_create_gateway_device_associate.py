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
    """���������豸�����ӿ�"""

    # ��ִ��ǰ��ʼ
    @classmethod
    def setUpClass(cls):
        # �ر�https��֤��У��
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    @classmethod
    def tearDownClass(cls):
        pass

    # ����ǰ��ʼ
    def setUp(self):
        self.id_pro = id_pro
        self.id_dev = id_dev
        self.id_gateway = "10082804"
        self.url = url + '/devices/gateway/associations'
        self.accessKey = accessKeyId
        self.accessKeySecret = accessSecret
        self.headers = {
            'Content-Type': 'application/json',
            'platform': '3'
        }
        self.signatureNonce = int(time.time())

    def tearDown(self):
        pass

    def test_00(self):  # ִ���߼�::������Σ�������ȷ��д
        """���������豸����-�ɹ�"""
        params = {
            'accessKeyId': self.accessKey,
            'deviceIds': [self.id_dev],
            'gatewayId': self.id_gateway,
            'productId': self.id_pro,
            'signatureNonce': self.signatureNonce
        }
        body = {

        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=self.url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # ����Ӧ�Ľ�����ж���
        self.assertIn('true', r.text.lower())
        # print(r.text.lower())
        logging.info(f"case:���������豸����-�ɹ�\n�����ַ��{r.url}\t����ʽ:{r.request.method}\n"
                     f"����ͷ��{r.request.headers}\n�������ģ�{parse.unquote(r.request.body)}\n��Ӧͷ��{r.headers}\n��Ӧ���ģ�{r.text}\n")


if __name__ == '__main__':
    unittest.main()
