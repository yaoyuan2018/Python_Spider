import base64
import json
import requests
import urllib.request
"""
这里的token为前面请求等到的，params的参数中，图片需要base64编码
"""
access_token = '24.09b1e219d81f65261eb3b544cdeb0f29.2592000.1556092638.282335-15839547'

def get_img_base(file):
    with open(file,'rb') as fp:
        content = base64.b64encode(fp.read())
        return content


request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
request_url = request_url + "?access_token=" + access_token

data = {
    'image':get_img_base('test.jpg'),
    'image_type':'BASE64',
    'face_field':'age,beauty,gender'
}
params = urllib.parse.urlencode(data).encode(encoding = 'UTF-8')
headers = {'Content-Type':'application/json'}
request = urllib.request.Request(url=request_url, data=params, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
if content:
    print(content)
    json_result = json.loads(content)
    print(json_result)
    code = json_result['error_code']
    gender = json_result['result']['face_list'][0]['gender']['type']
    beauty = json_result['result']['face_list'][0]['beauty']
    print(code,gender,beauty)
# request = requests.post(url=request_url,data=params)
# result = request.text
# json_result = json.loads(result)
# print(json_result)
# code = json_result['error_code']
# gender = json_result['result']['face_list'][0]['gender']['type']
# beauty = json_result['result']['face_list'][0]['beauty']
# print(code,gender,beauty)