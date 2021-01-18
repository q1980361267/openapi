import requests
from assist.getSignature import get_signature
import time
import json
import urllib3
import logging
from assist.get_color import color
from config import global_environment
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

config_file = global_environment.configFilePath()
assist_file = global_environment.assistFilePath()

with open(config_file, 'r') as f:
    f_json = json.load(f)
    url = f_json.get("baseURL")
    # accessKeyId = f_json.get("accessKeyId")
    accessKeySecret = f_json.get("secret")


def get_projectId(accessKeyId, accessKeySecret):
    headers ={}
    body = {

        }

    params = {
        'accessKeyId': accessKeyId,
        'signatureNonce': int(time.time() * 1000),
        # 'projectName': 'IOT'
    }

    _url = "https://iotapi.sit.cmft.com/oes/api/v1/auth/project"
    signature = get_signature(params, body, accessKeySecret, 'GET')
    params['signature'] = signature

    r = requests.get(url=_url, params=params, data=json.dumps(body), headers=headers, verify=False)
    try:
        result = r.json()
        data = result.get('data')
        projectId = data[0].get("projectId")
        if "true" in r.text:
            return projectId
        else:
            print('{}'.format(result))
            sys.exit(-1)
    except Exception:
        print(color.red('{}'.format(r.text)))


if __name__ == '__main__':

    # accessKeySecret = "cGIw0NFnne4wN56V"
    accessKeyId = "cGIw0NFnne4wN56V"
    a = get_projectId(accessKeyId, accessKeySecret)
    print(a)
