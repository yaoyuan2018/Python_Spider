from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    target = 'https://unsplash.com/'
    req = requests.get(target)
    print(req.text)