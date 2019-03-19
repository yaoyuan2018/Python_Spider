from bs4 import BeautifulSoup
import requests

"""
测试文件：瞎几把测试
"""

if __name__ == '__main__':
    req = requests.get('http://www.luoxia.com/modu/91504.htm')
    html = req.text
    div_bf = BeautifulSoup(html)
    div = div_bf.find_all('div', id='nr1')
    texts = div[0].text.replace('\n',"\n\n")

    # print(div[0].text)
    print(texts)