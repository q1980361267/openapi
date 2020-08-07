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

with open("../../test_config.json", 'r') as f:
    f_json = json.load(f)
    url = f_json.get("baseURL")
    accessKeyId = f_json.get("accessKeyId")
    accessSecret = f_json.get("secret")


# with open('../../assist_config.yaml', 'r') as f:
#     data = yaml.load(f, Loader=yaml.FullLoader)
#     id_gateway = data.get('ecp_node_deviceId')
#     id_dev = data.get('ecp_deviceId')
#     id_pro = data.get('ecp_productId')

class Test_Router(unittest.TestCase):
    """Ŀ�ĵ����ýӿ�"""

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
        """����·��Ŀ�ĵض˵�-�ɹ�"""
        _url = url + '/address-configs/connection/testing'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            "name": "mysql",
            "type": 4,
            "env": 1,
            "host": "36.155.103.36",
            "port": 3306,
            "username": "root",
            "password": "Iot!@10086",
            "database": "edgetester",
            "table": "test"
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # ����Ӧ�Ľ�����ж���
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:��ѯ��ǩ-�ɹ�\n�����ַ��{r.url}\t����ʽ:{r.request.method}\n"
                     f"����ͷ��{r.request.headers}\n�������ģ�{parse.unquote(r.request.body)}\n��Ӧͷ��{r.headers}\n��Ӧ���ģ�{r.text}\n")

    def test_01(self):  # ִ���߼�::������Σ�������ȷ��д
        """����·��Ŀ�ĵض˵�-�ɹ�"""
        _url = url + '/address-configs'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {
            "name": "mysql_" + ''.join(random.sample('123456abcdef', 5)),
            "type": 4,
            "env": 1,
            "host": "36.155.103.36",
            "port": 3306,
            "username": "root",
            "password": "Iot!@10086",
            "database": "edgetester",
            "table": "test"
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # ����Ӧ�Ľ�����ж���
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:��ѯ��ǩ-�ɹ�\n�����ַ��{r.url}\t����ʽ:{r.request.method}\n"
                     f"����ͷ��{r.request.headers}\n�������ģ�{parse.unquote(r.request.body)}\n��Ӧͷ��{r.headers}\n��Ӧ���ģ�{r.text}\n")

    def test_02(self):  # ִ���߼�::������Σ�������ȷ��д
        """�޸�·��Ŀ�ĵض˵�-�ɹ�"""
        _url = url + '/address-configs/14239'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {}
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'PATCH')
        params['signature'] = signature
        r = requests.patch(url=_url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # ����Ӧ�Ľ�����ж���
        print(_url)
        print(r.json())
        self.assertIn('true', r.text.lower())

        logging.info(f"case:��ѯ��ǩ-�ɹ�\n�����ַ��{r.url}\t����ʽ:{r.request.method}\n"
                     f"����ͷ��{r.request.headers}\n�������ģ�{parse.unquote(r.request.body)}\n��Ӧͷ��{r.headers}\n��Ӧ���ģ�{r.text}\n")

    def test_03(self):  # ִ���߼�::������Σ�������ȷ��д
        """��ȡ·��Ŀ�ĵض˵�-�ɹ�"""
        _url = url + '/address-configs/14239'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
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

        logging.info(f"case:��ѯ��ǩ-�ɹ�\n�����ַ��{r.url}\t����ʽ:{r.request.method}\n"
                     f"����ͷ��{r.request.headers}\n�������ģ�{parse.unquote(r.request.body)}\n��Ӧͷ��{r.headers}\n��Ӧ���ģ�{r.text}\n")

    def test_04(self):  # ִ���߼�::������Σ�������ȷ��д
        """��ҳ��ѯ·��Ŀ�ĵض˵�-�ɹ�"""
        _url = url + '/address-configs'
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
            'type': 0,
            'currentPage': 1,
            'pageSize': 10
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

        logging.info(f"case:��ѯ��ǩ-�ɹ�\n�����ַ��{r.url}\t����ʽ:{r.request.method}\n"
                     f"����ͷ��{r.request.headers}\n�������ģ�{parse.unquote(r.request.body)}\n��Ӧͷ��{r.headers}\n��Ӧ���ģ�{r.text}\n")


if __name__ == '__main__':
    unittest.main()
