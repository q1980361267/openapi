# coding:gbk
from urllib import parse
import unittest
import time
import requests
import logging
import urllib3
import json

from assist import getOpenApiPramsTemplate, getSignature, getTemplateInfo


class Test_CreateGatewayDeviceAssociate(unittest.TestCase):
    """ģ���д������ܽӿ�"""

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
        self.id_group = getTemplateInfo.getTemplateId()
        self.url = getOpenApiPramsTemplate.get_url() + '/objtemplate/id/' + str(self.id_group)
        self.accessKey = getOpenApiPramsTemplate.getAccesskey()
        self.accessKeySecret = getOpenApiPramsTemplate.getAccessKeySecret()
        self.headers = getOpenApiPramsTemplate.getHeaders()
        self.signatureNonce = int(time.time())

    def tearDown(self):
        pass

    def test_00(self):  # ִ���߼�::������Σ�������ȷ��д
        """ģ���д�������-�ɹ�"""
        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce
        }
        body = {

        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'DELETE')
        params['signature'] = signature
        r = requests.delete(url=self.url, params=params, data=json.dumps(body), headers=self.headers)
        # success = r.json()['success']
        # ����Ӧ�Ľ�����ж���
        self.assertIn('true', r.text.lower())
        # print(r.text.lower())
        logging.info(f"case:ģ���д�������-�ɹ�\n�����ַ��{r.url}\t����ʽ:{r.request.method}\n����ͷ��{r.request.headers}\n�������ģ�{parse.unquote(r.request.body)}\n��Ӧͷ��{r.headers}\n��Ӧ���ģ�{r.text}\n")


if __name__ == '__main__':
    unittest.main()
