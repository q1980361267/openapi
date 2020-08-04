from urllib import parse
import json
import base64
import hmac
import binascii
from hashlib import sha1


def percentCode(value):
    try:
        value_solve = parse.quote(value, encoding='UTF-8')
        value_final = value_solve.replace("+", "%20").replace("*", "%2A"). \
            replace("%7E", "~").replace('/', '%2F').replace('=', '%3D')

        return value_final
    except Exception:
        return ''


def get_signature(params, body, accessKeySecret, method):
    """获得signature签名"""
    # params = {
    #     'signatureNonce':927,
    #     'accessKeyId':'aHfAI2D9YauyGmIF'
    # }
    # 参数编码
    ordered_params = parse.urlencode(params)
    # print(ordered_params)
    # 参数加上body编码
    # body = {
    #     'name':'abcd',
    #     'description':'abcd'
    # }
    if body:
        params_and_body = ordered_params + json.dumps(body)
    else:
        params_and_body = ordered_params
    # print(params_and_body)
    # ordered_params_and_body = percentCode(params_and_body)
    # print('no change:'+params_and_body)
    # print('change:'+ordered_params_and_body)
    # print('canonicalQueryString:'+params_and_body)

    # 整个请求
    whole_request_method = (method + '&' + percentCode('/') + '&' + percentCode(params_and_body))
    # print('stringToSign:'+ whole_request_method)
    # print("connect_param: ", whole_request_method)

    key = accessKeySecret
    msg = whole_request_method



    digest_whole_request_method = hmac.new(key=key.encode(), msg=msg.encode(), digestmod='sha1')
    # a= list(digest_whole_request_method.digest())

    # print(a)

    # print(binascii.hexlify(digest_whole_request_method.digest()))
    # print(digest_whole_request_method.digest())
    # print(digest_whole_request_method.hexdigest())
    signature_before_code = base64.b64encode(digest_whole_request_method.digest()).decode()
    # print("signature before: ", signature_before_code)
    # signature = signature_before_code
    # signature = percentCode(signature_before_code)
    signature = signature_before_code.replace('+', "").replace("=", "").replace('/', "")
    # print(base64.b64encode(digest_whole_request_method.digest()))
    # print(signature)
    return signature


# if __name__ == '__main__':
#     body = {
#         "name": "any content"
#     }
#
#     params = {
#         "accessKeyId":"jNn7WmVg4ZakCe2i",
#         "currentPage":1,
#         "pageSize":5,
#         "signatureNonce":11,
#         "type":0
#
#     }
#
#     accessKeySecret = "7436457567"
#     a = get_signature(params=params, body=body, accessKeySecret=accessKeySecret, method='PUT')
#     print(a)
#     print(('POST&%2F&accessKeyId%3D9ad6UCsoQOO0aMLp%26signatureNonce%3D5cc99f25-471c-4ad4-8ea9-661c7b2e05ad%7B%22name%22%3A%22modbus_model985%22%2C%22protocolType%22%3A4%7D'))


