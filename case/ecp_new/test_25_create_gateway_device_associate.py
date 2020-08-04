# coding:gbk
from urllib import parse
import unittest
import time
import requests
import logging
import urllib3
import json

from assist import getOpenApiPramsTemplate, getSignature, getDeviceInfo, getGatewayProductInfo,getGatewayDeviceInfo


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
        self.id_pro = getGatewayProductInfo.getGatewayProductId()
        self.id_dev_first = getDeviceInfo.getGatewayDevicesId()
        self.id_dev_second = getDeviceInfo.getGatewayDevicesIdSecond()
        self.id_gateway = getGatewayDeviceInfo.getDevicesId()
        self.url = getOpenApiPramsTemplate.get_url() + '/devices/gateway/associations'
        self.accessKey = getOpenApiPramsTemplate.getAccesskey()
        self.accessKeySecret = getOpenApiPramsTemplate.getAccessKeySecret()
        self.headers = getOpenApiPramsTemplate.getHeaders()
        self.signatureNonce = int(time.time())

    def tearDown(self):
        pass

    def test_00(self):  # ִ���߼�::������Σ�������ȷ��д
        """���������豸����-�ɹ�"""
        params = {
            'accessKeyId': self.accessKey,
            'deviceIds': [self.id_dev_first, self.id_dev_second],
            'gatewayId': self.id_gateway,
            'productId': self.id_pro,
            'signatureNonce': self.signatureNonce
        }
        body = {

        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=self.url, params=params, data=json.dumps(body), headers=self.headers)
        # success = r.json()['success']
        # ����Ӧ�Ľ�����ж���
        self.assertIn('true', r.text.lower())
        # print(r.text.lower())
        logging.info(f"case:���������豸����-�ɹ�\n�����ַ��{r.url}\t����ʽ:{r.request.method}\n����ͷ��{r.request.headers}\n�������ģ�{parse.unquote(r.request.body)}\n��Ӧͷ��{r.headers}\n��Ӧ���ģ�{r.text}\n")


if __name__ == '__main__':
    unittest.main()
