# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse as parse
from bs4 import BeautifulSoup
from selenium import webdriver
from .times import times_mk


def crawling(search):
    API = "http://find.mk.co.kr/new/search.php"
    values = {
        'pageNum':'1',
        'cat':'',
        'cat1':'',
        'media_eco':'',
        'pageSize':'20',
        'sub':'news',
        'dispFlag':'OFF',
        'page':'news',
        's_kwd':search,
        's_page':'total',
        'go_page':'',
        'ord':'1',
        'ord1':'1',
        'ord2':'0',
        's_keyword':search,
        'y1':'1991',
        'm1':'01',
        'd1':'01',
        'y2':'2020',
        'm2':'01',
        'd2':'20',
        'area':'ttbd'
    }
    params = parse.urlencode(values)
    url = API + '?' + params
    response = urllib.request.urlopen(url)
    content = response.read().decode('euc-kr','replace').encode('utf-8','replace') # 한글 깨짐으로 인함 https://m.blog.naver.com/PostView.nhn?blogId=binsoore&logNo=220666303601&proxyReferer=https%3A%2F%2Fwww.google.com%2F 참조
    soup = BeautifulSoup(content,"html.parser")
    results = soup.select(" div > span.art_tit > a")
    title = []
    page = []
    for result in results: title.append(result.text)
    for i in range(len(results)): page.append(results[i]['href'])
    data = times_mk.search(page)

    return title, page, data