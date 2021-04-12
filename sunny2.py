from bs4 import BeautifulSoup
import requests

import sys

args = sys.argv[1:]
d, m, y, sex = args

with open('simso.txt') as f:
    for line in f:
        sim = line.strip()
        URL = fr"https://www.simphongthuy.com/?do=xemdiemsim&sosim={sim}&ngaysinh={d}&thangsinh={m}&namsinh={y}&gioitinh={sex}&submit=1"

        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        mark = soup.find(attrs={"class": "x-diemsim-diem"}).text
        if float(mark.partition("/")[0].strip()) > 8:
            print(f"{sim} - [{mark}]")
