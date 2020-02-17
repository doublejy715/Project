import urllib.request
import urllib.parse as parse
from bs4 import BeautifulSoup
from .times import times_hankookilbo

def crawling(search):
    API = "https://hankookilbo.com/Search"
    values = {
            'Page':'',
            'q': search,
            'c':'',
            's':'1',
            'from':'2020-01-12',
            'until':''
    }
    params = parse.urlencode(values)
    url = API + '?' + params
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response,"html.parser")
    results = soup.select("div > div > ul > li > div > a > p.title ")
    title, page = list(),list()
    for result in results: title.append(result.text)
    li = soup.select("div > div > ul > li.item > div.body > a")
    for i in range(len(li)): page.append('https://www.hankookilbo.com'+li[i]['href'])
    data = times_hankookilbo.search(page)

    return title, page, data
