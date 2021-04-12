from bs4 import BeautifulSoup
import requests

import sys

args = sys.argv[1:]
diem, d, m, y, sex, *h = args

h = h[0] if h else 6

with open('simso.txt') as f:
    for line in f:
        sim = line.strip()

        page = requests.post(r"https://simphongthuy.vn/xem-phong-thuy-sim", files=dict(
            so_sim=(None, sim),
            ngay_sinh=(None, d),
            thang_sinh=(None, m),
            nam_sinh=(None, y),
            gio_sinh=(None, h),
            gioi_tinh=(None, sex)
        ))

        soup = BeautifulSoup(page.content, 'html.parser')
        mark = soup.find(attrs={"class": "luan_sim_ket_luan"}).text.split("\n")[1].split()[-1].split("/")[0]
        if float(mark) >= float(diem):
            print(f"{sim} - [{mark}/10]")
