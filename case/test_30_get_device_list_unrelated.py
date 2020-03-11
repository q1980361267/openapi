# coding:gbk
from urllib import parse
import unittest
import time
import requests
import logging
import urllib3
import json

from lib import getOpenApiPramsTemplate, getSignature, getGatewayDeviceInfo, getGatewayProductInfo


class Test_CreateGatewayDeviceAssociate(unittest.TestCase):
    """ɾ�������豸�����ӿ�"""

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
        self.id_product = getGatewayProductInfo.getGatewayProductId()
        self.id_gateway = getGatewayDeviceInfo.getDevicesId()
        self.url = getOpenApiPramsTemplate.get_url() + '/devices/subdevice/NIN/page'
        self.accessKey = getOpenApiPramsTemplate.getAccesskey()
        self.accessKeySecret = getOpenApiPramsTemplate.getAccessKeySecret()
        self.headers = getOpenApiPramsTemplate.getHeaders()
        self.signatureNonce = int(time.time())

    def tearDown(self):
        pass

    def test_00(self):  # ִ���߼�::������Σ�������ȷ��д
        """ɾ�������豸����-�ɹ�"""
        params = {
            'accessKeyId': self.accessKey,
            'currentPage': 1,
            'parentId': self.id_gateway,
            'pageSize': 10,
            'product': self.id_product,
            'protocol': 1,
            'gatewayId': self.id_gateway,
            'signatureNonce': self.signatureNonce
        }
        body = {

        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'GET')
        params['signature'] = signature
        r = requests.get(url=self.url, params=params, data=json.dumps(body), headers=self.headers)
        # success = r.json()['success']
        # ����Ӧ�Ľ�����ж���
        self.assertIn('true', r.text.lower())
        # print(r.text.lower())
        logging.info(f"case:ɾ�������豸����-�ɹ�\n�����ַ��{r.url}\t����ʽ:{r.request.method}\n����ͷ��{r.request.headers}\n�������ģ�{parse.unquote(r.request.body)}\n��Ӧͷ��{r.headers}\n��Ӧ���ģ�{r.text}\n")


if __name__ == '__main__':
    unittest.main()
