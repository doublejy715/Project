import re
import urllib.request  as req
import urllib.parse as parse
from bs4 import BeautifulSoup as bs

def daum_list():
    url = "https://www.daum.net"
    response = req.urlopen(url)
    soup = bs(response, 'html.parser')
    newest = soup.select('a.link_issue')
    data = set()
    for new in newest:
        data.add(new.text)

    return data
