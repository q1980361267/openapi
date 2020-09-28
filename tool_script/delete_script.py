import gevent
import urllib3
import requests
from assist import getSignature
import time
import json
import sys
import logging
from assist.get_color import color

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open('../config/pre_config.json') as f:
    f_json = json.load(f)
    addr = f_json.get('baseURL')
    accessKeyId = f_json.get('accessKeyId')
    accessKeySecret = f_json.get('secret')

headers = {
    'Content-Type': 'application/json',
    'platform': '3'
}


def check_product_id():
    url = addr + '/products'
    global headers
    headers = headers

    params = {
        'accessKeyId': accessKeyId,
        'signatureNonce': int(time.time() * 1000),
        'pageSize': 10,
        'currentPage': 1
    }

    body = {

    }

    signature = getSignature.get_signature(params, body, accessKeySecret, 'GET')
    params['signature'] = signature
    r = requests.get(url=url, params=params, data=json.dumps(body), headers=headers, verify=False)
    try:
        content = r.json().get('data').get('content')
        id = content[0].get('id')
        return id
    except Exception:
        print(r.text)


def delete_product(id):
    url = addr + '/products/' + str(id)
    global headers
    headers = headers

    params = {
        'accessKeyId': accessKeyId,
        'signatureNonce': int(time.time() * 1000)

    }

    body = {

    }

    signature = getSignature.get_signature(params, body, accessKeySecret, 'DELETE')
    params['signature'] = signature
    r = requests.delete(url=url, params=params, data=json.dumps(body), headers=headers, verify=False)


def check_rule_id():
    url = addr + '/rules'
    global headers
    headers = headers

    params = {
        'accessKeyId': accessKeyId,
        'signatureNonce': int(time.time() * 1000),
        'pageSize': 50,
        'currentPage': 1,
        'type': 1
    }

    body = {

    }

    signature = getSignature.get_signature(params, body, accessKeySecret, 'GET')
    params['signature'] = signature
    r = requests.get(url=url, params=params, data=json.dumps(body), headers=headers, verify=False)
    # print(r.json())

    try:
        content = r.json().get('data').get('content')
        id = content[0].get('id')
        return id
    except Exception:
        print(r.text)


def delete_rule(rule_id):
    url = addr + '/rules/' + str(rule_id)
    global headers
    headers = headers

    params = {
        'accessKeyId': accessKeyId,
        'signatureNonce': int(time.time() * 1000)

    }

    body = {

    }

    signature = getSignature.get_signature(params, body, accessKeySecret, 'DELETE')
    params['signature'] = signature
    r = requests.delete(url=url, params=params, data=json.dumps(body), headers=headers, verify=False)


def check_node_id():
    url = addr + '/edgenode/pro/page'
    global headers
    headers = headers

    params = {
        'accessKeyId': accessKeyId,
        'signatureNonce': int(time.time() * 1000),
        'pageSize': 10,
        'currentPage': 1
    }

    body = {}

    signature = getSignature.get_signature(params, body, accessKeySecret, 'GET')
    params['signature'] = signature
    r = requests.get(url=url, params=params, data=json.dumps(body), headers=headers, verify=False)
    content = r.json().get('data').get('content')
    try:
        id = content[0].get('id')
        return id
    except Exception:
        raise


def delete_node(id):
    url = addr + '/edgenode/pro/{}'.format(id)
    global headers
    headers = headers

    params = {
        'accessKeyId': accessKeyId,
        'signatureNonce': int(time.time() * 1000)

    }

    body = {}

    signature = getSignature.get_signature(params, body, accessKeySecret, 'DELETE')
    params['signature'] = signature
    r = requests.delete(url=url, params=params, data=json.dumps(body), headers=headers, verify=False)


def check_destination_id():
    url = addr + '/address-configs'
    global headers
    headers = headers

    params = {
        'accessKeyId': accessKeyId,
        'signatureNonce': int(time.time() * 1000),
        'pageSize': 10,
        'currentPage': 1,
        'type': 0
    }

    body = {}

    signature = getSignature.get_signature(params, body, accessKeySecret, 'GET')
    params['signature'] = signature
    r = requests.get(url=url, params=params, data=json.dumps(body), headers=headers, verify=False)
    content = r.json().get('data').get('content')
    try:
        id = content[0].get('id')
        return id
    except Exception:
        pass


def delete_destination(id):
    url = addr + '/address-configs/{}'.format(id)
    global headers
    headers = headers

    params = {
        'accessKeyId': accessKeyId,
        'signatureNonce': int(time.time() * 1000)

    }

    body = {}

    signature = getSignature.get_signature(params, body, accessKeySecret, 'DELETE')
    params['signature'] = signature
    r = requests.delete(url=url, params=params, data=json.dumps(body), headers=headers, verify=False)

def check_router_id():
    url = addr + '/routers'
    global headers
    headers = headers

    params = {
        'accessKeyId': accessKeyId,
        'signatureNonce': int(time.time() * 1000),
        'pageSize': 10,
        'currentPage': 1
    }

    body = {}

    signature = getSignature.get_signature(params, body, accessKeySecret, 'GET')
    params['signature'] = signature
    r = requests.get(url=url, params=params, data=json.dumps(body), headers=headers, verify=False)
    content = r.json().get('data').get('content')
    try:
        id = content[0].get('id')
        return id
    except Exception:
        pass


def delete_router(id):
    url = addr + '/routers/{}'.format(id)
    global headers
    headers = headers

    params = {
        'accessKeyId': accessKeyId,
        'signatureNonce': int(time.time() * 1000)

    }

    body = {}

    signature = getSignature.get_signature(params, body, accessKeySecret, 'DELETE')
    params['signature'] = signature
    r = requests.delete(url=url, params=params, data=json.dumps(body), headers=headers, verify=False)

def check_mail_id():
    url = addr + '/mail/server/query/page'
    global headers
    headers = headers

    params = {
        'accessKeyId': accessKeyId,
        'signatureNonce': int(time.time() * 1000)
    }

    body = {
            "currentPage": 1,
            "pageSize": 10
        }

    signature = getSignature.get_signature(params, body, accessKeySecret, 'GET')
    params['signature'] = signature
    r = requests.get(url=url, params=params, data=json.dumps(body), headers=headers, verify=False)
    content = r.json().get('data').get('content')
    try:
        id = content[0].get('id')
        return id
    except Exception:
        pass


def delete_mail(id):
    url = addr + '/mail/server/id/{}'.format(id)
    global headers
    headers = headers

    params = {
        'accessKeyId': accessKeyId,
        'signatureNonce': int(time.time() * 1000)

    }

    body = {}

    signature = getSignature.get_signature(params, body, accessKeySecret, 'DELETE')
    params['signature'] = signature
    r = requests.delete(url=url, params=params, data=json.dumps(body), headers=headers, verify=False)

def check_template_id():
    url = addr + '/mail/pattern/query/page'
    global headers
    headers = headers

    params = {
        'accessKeyId': accessKeyId,
        'signatureNonce': int(time.time() * 1000)
    }

    body = {
            "currentPage": 1,
            "pageSize": 10
        }

    signature = getSignature.get_signature(params, body, accessKeySecret, 'GET')
    params['signature'] = signature
    r = requests.get(url=url, params=params, data=json.dumps(body), headers=headers, verify=False)
    content = r.json().get('data').get('content')
    try:
        id = content[0].get('id')
        return id
    except Exception:
        pass


def delete_template(id):
    url = addr + '/mail/pattern/id/{}'.format(id)
    global headers
    headers = headers

    params = {
        'accessKeyId': accessKeyId,
        'signatureNonce': int(time.time() * 1000)

    }

    body = {}

    signature = getSignature.get_signature(params, body, accessKeySecret, 'DELETE')
    params['signature'] = signature
    r = requests.delete(url=url, params=params, data=json.dumps(body), headers=headers, verify=False)






if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    while True:
        id = check_product_id()
        if id:
            delete_product(id)
        else:
            break
    logging.info(color.cyan('删除产品完成'))

    while True:
        rule_id = check_rule_id()
        if rule_id:
            delete_rule(rule_id)
        else:
            break
    logging.info(color.cyan('删除规则完成'))

    # while True:
    #     router_id = check_router_id()
    #     if router_id:
    #         delete_router(router_id)
    #     else:
    #         break
    # logging.info(color.cyan('删除路由实例完成'))
    #
    # while True:
    #     destination_id = check_destination_id()
    #     if destination_id:
    #         delete_destination(destination_id)
    #     else:
    #         break
    # logging.info(color.cyan('删除目的地完成'))
    #
    # while True:
    #     mail_id = check_mail_id()
    #     if mail_id:
    #         delete_router(mail_id)
    #     else:
    #         break
    # logging.info(color.cyan('删除邮件服务器完成'))
    #
    # while True:
    #     template_id = check_template_id()
    #     if template_id:
    #         delete_template(template_id)
    #     else:
    #         break
    # logging.info(color.cyan('删除邮件模板完成'))
    #
    # while True:
    #     node_id = check_node_id()
    #     if node_id:
    #         delete_node(node_id)
    #     else:
    #         break
    # logging.info(color.cyan('删除节点完成'))