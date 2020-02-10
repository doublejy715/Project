import urllib.request
import urllib.parse as parse
from bs4 import BeautifulSoup
from selenium import webdriver

print("검색할 단어를 적어 주세요 : ")
search = input()
print(search)
# 서울일보의 검색 뉴스들의 제목을 끌어다 오기
API = "https://search.hankyung.com/apps.frm/search.news"
# 순서대로 2차 튜플을 만들어서 각 신문사로 넘겨준다.
values = {
    'query':search,
    'mediaid_clust':'HKPAPER,HKCOM'
}
params = parse.urlencode(values)
url = API + '?' + params
print(url)

# 검색창을 하나 가져온다.
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response,"html.parser")
results = soup.select("#content > div > div > div > div > ul > li > div > a > em")

for result in results:
    print(result.string)

# 출력 형태를 가공할 필요가 있음