
import requests
import urllib.request as req
import urllib.parse as parse
from bs4 import BeautifulSoup
 
url = "https://www.naver.com/"
headers = {'User-Agent': 'Mozilla/5.0'}
reqUrl = req.Request(url,headers=headers)
res = req.urlopen(reqUrl)
soup = BeautifulSoup(res, "html.parser")
text = soup.select('li.ah_item > a')

print(text)