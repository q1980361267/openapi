# coding:gbk
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

class Test_Router(unittest.TestCase):
    """����·�ɽӿ�"""

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
        # self.id_pro = id_pro
        # self.id_gateway = "10082804"
        self.url = url
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
        """����·��ʵ����ĳ��Ե�ڵ�-�ɹ�"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('ecp_node_deviceId')
            id_router = data.get('edge_router_id')

        _url = self.url + '/routers/gateway/association'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            'devId': str(id_dev),
            'exportClientId': [id_router]
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # ����Ӧ�Ľ�����ж���
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:����·��ʵ����ĳ��Ե�ڵ�-�ɹ�\n�����ַ��{r.url}\t����ʽ:{r.request.method}\n"
                     f"����ͷ��{r.request.headers}\n�������ģ�{parse.unquote(r.request.body)}\n��Ӧͷ��{r.headers}\n��Ӧ���ģ�{r.text}\n")

    def test_01(self):  # ִ���߼�::������Σ�������ȷ��д
        """��ҳ��ѯ�ѷ�������Ե�ڵ��·��ʵ��-�ɹ�"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('ecp_node_deviceId')

        _url = url + '/routers/gateway/association'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'currentPage': 1,
            'pageSize': 10,
            'deviceId': id_dev
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # ����Ӧ�Ľ�����ж���
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:��ҳ��ѯ�ѷ�������Ե�ڵ��·��ʵ��-�ɹ�\n�����ַ��{r.url}\t����ʽ:{r.request.method}\n"
                     f"����ͷ��{r.request.headers}\n�������ģ�{parse.unquote(r.request.body)}\n��Ӧͷ��{r.headers}\n��Ӧ���ģ�{r.text}\n")

    def test_03(self):  # ִ���߼�::������Σ�������ȷ��д
        """��ҳ��ѯδ�����·��ʵ����Ϣ-�ɹ�"""
        with open(assist_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            id_dev = data.get('ecp_node_deviceId')

        _url = url + '/routers/gateway/unassignedclient'

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'currentPage': 1,
            'pageSize': 10,
            'deviceId': id_dev
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # ����Ӧ�Ľ�����ж���
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:��ҳ��ѯδ�����·��ʵ����Ϣ-�ɹ�\n�����ַ��{r.url}\t����ʽ:{r.request.method}\n"
                     f"����ͷ��{r.request.headers}\n�������ģ�{parse.unquote(r.request.body)}\n��Ӧͷ��{r.headers}\n��Ӧ���ģ�{r.text}\n")


if __name__ == '__main__':
    unittest.main()
