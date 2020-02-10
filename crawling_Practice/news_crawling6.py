
import urllib.request
import urllib.parse as parse
from bs4 import BeautifulSoup
from selenium import webdriver

print("검색할 단어를 적어 주세요 : ")
search = input()
print(search)
# 서울일보의 검색 뉴스들의 제목을 끌어다 오기
API = "http://find.mk.co.kr/new/search.php"
# 순서대로 2차 튜플을 만들어서 각 신문사로 넘겨준다.
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
print(url)

# 검색창을 하나 가져온다.
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response,"html.parser")
results = soup.select("body > center > table > tbody > tr > td > div > span > a")

for result in results:
    print(result.string)

# 출력 형태를 가공할 필요가 있음