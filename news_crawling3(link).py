
import urllib.request
import urllib.parse as parse
from bs4 import BeautifulSoup

print("검색할 단어를 적어 주세요 : ")
search = input()
print(search)
# 서울일보의 검색 뉴스들의 제목을 끌어다 오기
API = "http://search.khan.co.kr/search.html"
# 순서대로 2차 튜플을 만들어서 각 신문사로 넘겨준다.
values = {
    'stb':'',
    'q':search
}
params = parse.urlencode(values)
url = API + '?' + params
print(url)

# 검색창을 하나 가져온다.
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response,"html.parser")
results = soup.select("div#container > div > div > dl > dt > a ")

for result in results:
    print(result.string)
    # 링크 어떻게 따오지
    r1 = result.attrib['href']
    print(r1)
