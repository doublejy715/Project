
import urllib.request
import urllib.parse as parse
from bs4 import BeautifulSoup
from .times import times_khan

def crawling(search):
    API = "http://search.khan.co.kr/search.html"
    values = {
        'stb':'khan',
        'q':search
    }
    params = parse.urlencode(values)
    url = API + '?' + params
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response,"html.parser")
    results = soup.select("#container > div.content > div.news.section > dl > dt > a")
    title, page = list(), list()
    for result in results: title.append(result.text)
    for i in range(len(results)): page.append(results[i]['href'])
    data = times_khan.search(page)

    return title, page, data
