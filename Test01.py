import requests
from bs4 import BeautifulSoup

"""
教程案例测试
"""

if __name__ == '__main__':
    url = 'http://gitbook.cn/'
    req = requests.get(url)
    html = req.text
    bf = BeautifulSoup(html,features="html.parser")
    texts = bf.find_all('div', class_ = 'chat_info_bottom')
    # print(texts)
    # print(texts[0])
    print(texts[0].text.replace('\xa0'*8,'\n\n'))
