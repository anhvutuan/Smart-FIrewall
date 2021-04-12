from bs4 import BeautifulSoup
import requests


TOTAL_PAGE = 1_000
ROOT_URL = r"https://www.thegioididong.com/sim-so-dep/vietnamobile?t=59&trang="

urls = (f"{ROOT_URL}{i}" for i in range(1, TOTAL_PAGE + 1))

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


with open('simso.txt', 'w') as f:
    for url in urls:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')


        for i in soup.find_all(attrs={'class': 'width_1'}):
            span = i.span
            if not span:
                continue
            print(span.text.replace('.', ''), file=f)
