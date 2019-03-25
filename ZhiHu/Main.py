import requests
import os
import base64
import json
import time

def get_img_base(file):
    with open(file,'rb') as fp:
        content = base64.b64encode(fp.read())
        return content

file_path = 'row_img'
list_paths = os.listdir(file_path)
for list_path in list_paths:
    img_path = file_path + '/' + list_path
    print(img_path)

    token = '24.a2d7a4d09435e716cf1cb163f176cb12.2592000.1553929524.282335-15648650'

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    request_url = request_url + "?access_token=" + token

    params = {
        'image': get_img_base(img_path),
        'image_type' : 'BASE64',
        'face_field' : 'age,beauty,gender'
    }

    res = requests.post(request_url, data=params)
    json_result = json.loads(res.text)
    code = json_result['error_code']

    if code == 22202:
        continue

    try:
        gender = json_result['result']['face_list'][0]['gender']['type']
        if gender == 'male':
            continue
        beauty = json_result['result']['face_list'][0]['beauty']
        new_beauty = round(beauty/10,1)
        print(img_path,new_beauty)
        if new_beauty >= 8:
            os.rename(os.path.join(file_path,list_path),os.path.join("8分",str(new_beauty) + "+" + list_path))
        elif new_beauty >= 7:
            os.rename(os.path.join(file_path,list_path),os.path.join("7分",str(new_beauty) + "+" + list_path))
        elif new_beauty >= 6:
            os.rename(os.path.join(file_path, list_path), os.path.join("6分", str(new_beauty) + "+" + list_path))
        elif new_beauty >= 5:
            os.rename(os.path.join(file_path, list_path), os.path.join("5分", str(new_beauty) + "+" + list_path))
        else:
            os.rename(os.path.join(file_path, list_path), os.path.join("其他分", str(new_beauty) + "+" + list_path))
        time.sleep(1)

    except KeyError:
        pass
    except TypeError:
        pass