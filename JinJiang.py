from bs4 import BeautifulSoup
import requests,sys

"""
类说明： 下载"落霞小说"网《默读》
Parameters:
    无
Returns：
    无
Modify:
    2019-03-19
"""
class downloader(object):

    def __init__(self):
        self.server = 'http://www.luoxia.com/'
        self.target = 'http://www.luoxia.com/modu/'
        self.names = []         #存放章节名
        self.urls = []          #存放章节链接
        self.nums = 0           #章节数
    """
    函数说明：获取下载链接
    """
    def get_download_url(self):
        req = requests.get(url = self.target)
        html = req.text
        div_bf = BeautifulSoup(html,features="html.parser")
        div = div_bf.find_all('div', class_='book-list clearfix')
        a_bf = BeautifulSoup(str(div[0]),features="html.parser")
        a = a_bf.find_all('a')
        self.nums = len(a)                  #剔除不必要的章节，并统计章节数
        for each in a:
            self.names.append(each.string)
            self.urls.append(each.get('href'))

    """
    函数说明：获取章节内容
    """
    def get_contents(self, target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html,features="html.parser")
        texts = bf.find_all('div', id = 'nr1')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts
    """
    函数说明：将爬取的文章内容写入文件
        name - 章节名称(string)
        path - 当前路径下，小说保存名称(string)
        text - 章节内容(string)
    """
    def writer(self, name, path, text):
        write_flag = True
        with open(path,'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('《默读》开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i],'默读.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write(" 已下载：%.3f%%" % float(i/dl.nums) + '\r')
        sys.stdout.flush()

    print('《默读》下载完成')


