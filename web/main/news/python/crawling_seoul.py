import re
import urllib.request
import urllib.parse as parse
from bs4 import BeautifulSoup
from .times import times_seoul


def crawling(search):
    API = "http://search.seoul.co.kr/index.php"
    values = {
        'keyword':search
    }
    params = parse.urlencode(values)
    url = API + '?' + params
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response,"html.parser")
    results = soup.select("div > dl > dt > a ")
    title,page = list(), list()
    for result in results: title.append(result.text)
    for i in range(len(results)): page.append(results[i]['href'])
    data = times_seoul.search(page)

    return title, page, data