import urllib.request
import urllib.parse as parse
from bs4 import BeautifulSoup

print("검색할 단어를 적어 주세요 : ")
search = input()
print(search)
# 서울일보의 검색 뉴스들의 제목을 끌어다 오기
API = "http://search.seoul.co.kr/index.php"
# 순서대로 2차 튜플을 만들어서 각 신문사로 넘겨준다.
values = {
    'keyword':search
}
params = parse.urlencode(values)
url = API + '?' + params
print(url)

# 검색창을 하나 가져온다.
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response,"html.parser")
results = soup.select("div > dl > dt > a ")

for result in results:
    print(result.string)
