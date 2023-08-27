import pytest
import requests
from bs4 import BeautifulSoup
from utils.read_data import read_yaml

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
}


@pytest.mark.parametrize("start", read_yaml()['mobile_params'])
def test_mobile(start):
    url = "https://movie.douban.com/top250"
    params = {"start": start}
    r = requests.get(url=url, params=params, headers=headers)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    all_titles = soup.findAll("span", attrs={"class": "title"})
    print(r.status_code)
    assert r.status_code == 200
    for title in all_titles:
        title_string = title.string
        if "/" not in title_string:
            print(title_string)
