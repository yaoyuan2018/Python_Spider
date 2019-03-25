import requests
from lxml import etree
import json
import time
import re

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'cookie':''     #需填写自己的cooike
}

def get_img(url):
    res = requests.get(url, headers = headers)
    i = 1
    json_data = json.loads(res.text)
    datas = json_data['data']
    for data in datas:
        id = data['author']['name']
        content = data['content']
        imgs = re.findall('img src="(.*?)"',content.re.S)
        if len(imgs) == 0:
            pass
        else:
            for img in imgs:
                if 'jpg' in img:
                    res_1 = requests.get(img,headers = headers)
                    fp = open('row_img' + id + '+' + str(i) + '.jpg','wb')
                    fp.write(res_1.content)
                    i = i + 1
                    print(id,img)       #图片命名为用户昵称+数字(由于一个回答可能有多个图片)

if __name__ == '__main__':
    urls = [
        'https://www.zhihu.com/api/v4/questions/29024583/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset={}&platform=desktop&sort_by=default'
            .format(str(i))
        for i in range (0, 25000, 5)]

    for url in urls:
        get_img(url)
        time.sleep(2)

