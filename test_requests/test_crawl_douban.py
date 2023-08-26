import pytest
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
}


def test_mobile():
    for start_num in range(0, 25, 25):
        url = f"https://movie.douban.com/top250?start={start_num}"
        r = requests.get(url=url, headers=headers)
        html = r.text
        soup = BeautifulSoup(html, "html.parser")
        all_titles = soup.findAll("span", attrs={"class": "title"})
        print(r.status_code)
        assert r.status_code == 200
        for title in all_titles:
            title_string = title.string
            if "/" not in title_string:
                print(title_string)

                # # 将结果写入文件
                # with open("D:/Users/12828/Desktop/hi.txt", "a", encoding='utf-8') as f:
                #     f.write(title_string + "\n")
