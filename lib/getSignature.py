from urllib import parse
import json
import base64
import hmac
def percentCode(value):
    try:
        value_solve = parse.quote(value, encoding='UTF-8')
        value_final = value_solve.replace("+", "%20").replace("*", "%2A").replace("%7E", "~").replace('/', '%2F')
        return value_final
    except Exception:
        return ''
def get_signature(params,body,accessKeySecret,method):
    """获得signature签名"""
    # params = {
    #     'signatureNonce':927,
    #     'accessKeyId':'aHfAI2D9YauyGmIF'
    # }
    # 参数编码
    ordered_params = parse.urlencode(params)
    #参数加上body编码
    # body = {
    #     'name':'abcd',
    #     'description':'abcd'
    # }
    if body:
        params_and_body = ordered_params + json.dumps(body)
    else:
        params_and_body = ordered_params

    # ordered_params_and_body = percentCode(params_and_body)
    # print('no change:'+params_and_body)
    # print('change:'+ordered_params_and_body)
    # print('canonicalQueryString:'+params_and_body)


    #整个请求
    whole_request_method = method + '&' + percentCode('/') + '&' + percentCode(params_and_body)
    # print('stringToSign:'+ whole_request_method)



    key = accessKeySecret
    msg = whole_request_method
    digest_whole_request_method = hmac.new(key=key.encode(),msg=msg.encode(),digestmod='sha1')
    signature_before_code = base64.b64encode(digest_whole_request_method.digest()).decode()
    signature = percentCode(signature_before_code)
    # print(base64.b64encode(digest_whole_request_method.digest()))
    # print(signature)
    return signature
# if __name__ == '__main__':
#     body ={
#         "name":"modbus_model985",
#         "protocolType":4
#     }
#
#     params ={
#         "accessKeyId":"9ad6UCsoQOO0aMLp",
#         "signatureNonce":"5cc99f25-471c-4ad4-8ea9-661c7b2e05ad"
#     }
#
#     accessKeySecret = 'vLwSNdEOGwSTon2efTrtup7nBZZMtpPgLr38'
#     a=get_signature(params=params,body=body,accessKeySecret=accessKeySecret,method='POST')
    # print(a)
    # print(('POST&%2F&accessKeyId%3D9ad6UCsoQOO0aMLp%26signatureNonce%3D5cc99f25-471c-4ad4-8ea9-661c7b2e05ad%7B%22name%22%3A%22modbus_model985%22%2C%22protocolType%22%3A4%7D'))

