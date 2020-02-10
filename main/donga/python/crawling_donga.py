import urllib.request
import urllib.parse as parse
from bs4 import BeautifulSoup
from selenium import webdriver
from .times import times_donga

def crawling(search):
    API = "http://www.donga.com/news/search"
    values = {
        'check_news':'1',
        'more':'1',
        'sorting':'1',
        'range':'1',
        'search_date':'',
        'query':search
    }
    params = parse.urlencode(values)
    url = API + '?' + params
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response,"html.parser")
    results = soup.select("#contents > div.searchContWrap > div.searchCont > div > div.t > p.tit > a")
    title, page = list(),list()
    for result in results: title.append(result.text)
    for i in range(len(results)): page.append(results[i]['href'])
    data = times_donga.search(page)

    return title, page, data
