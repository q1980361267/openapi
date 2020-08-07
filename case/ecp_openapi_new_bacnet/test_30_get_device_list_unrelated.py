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
    """��ҳ��ѯ��Ե�ڵ�����ı�Ե�նˣ�NIN���ӿ�"""

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

    def test_00(self):  # ִ���߼�::������Σ�������ȷ��д
        """��ҳ��ѯ��Ե�ڵ�����ı�Ե�նˣ�NIN��-�ɹ�"""
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
        # ����Ӧ�Ľ�����ж���
        print(r.json())
        print(self.url)
        print(params)
        self.assertIn('true', r.text.lower())

        logging.info(f"case:��ҳ��ѯ��Ե�ڵ�����ı�Ե�նˣ�NIN��-�ɹ�\n�����ַ��{r.url}\t����ʽ:{r.request.method}\n"
                     f"����ͷ��{r.request.headers}\n�������ģ�{parse.unquote(r.request.body)}\n��Ӧͷ��{r.headers}\n��Ӧ���ģ�{r.text}\n")


if __name__ == '__main__':
    unittest.main()
