import urllib.request
import urllib.parse as parse
from bs4 import BeautifulSoup
from selenium import webdriver
from .times import times_hankyung

def crawling(search):
    API = "https://search.hankyung.com/apps.frm/search.news"
    values = {
        'query':search,
        'mediaid_clust':'HKPAPER,HKCOM'
    }
    params = parse.urlencode(values)
    url = API + '?' + params
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response,"html.parser")
    results = soup.select("#content > div > div > div > div > ul > li > div > a > em")
    title, page = list(), list()
    for result in results:
        if '"' in result:
            continue
        title.append(result.text[58:])
    li = soup.select("#content > div > div > div > div > ul > li > div > a")
    for i in range(len(results)): page.append(li[i]['href'])
    data = times_hankyung.search(page)

    return title, page, data