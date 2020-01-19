import urllib.request
import urllib.parse as parse
from bs4 import BeautifulSoup

print("검색할 단어를 적어 주세요 : ")
search = input()
print(search)
# 한국일보의 검색 뉴스들의 제목을 끌어다 오기
API = "https://hankookilbo.com/Search"
# 순서대로 2차 튜플을 만들어서 각 신문사로 넘겨준다.
values = {
        'Page':'',
        'q': search,
        'c':'',
        's':'1',
        'from':'2020-01-12',
        'until':'2020-01-19'
}
params = parse.urlencode(values)
url = API + '?' + params
print(url)
# 검색창을 하나 가져온다.
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response,"html.parser")
results = soup.select("div > div > ul > li > div > a > p ")

for result in results:
    print(result.string)

# 뭔가 이상한게 더 나온다.