import re
import urllib.request  as req
import urllib.parse as parse
from bs4 import BeautifulSoup as bs
import pickle

def daum_list():
    data = set()
    for index in range(1,1000):
        API = "https://people.joins.com/Search/default.aspx"
        values = {
            'ps':'',
            'q':'한국',
            'pgi':index,
        }
        params = parse.urlencode(values)
        url = API + '?' + params
        response = req.urlopen(url)
        soup = bs(response, 'html.parser')
        newest = soup.select('div.main > div > div.bd > ul > li > dl > dt > a')

        for new in newest:
            print(new.text) 

            if len(new.text) == 1:
                data.add(new.text)
            elif new.text[1] == '(':
                data.add(new.text[:1])
            elif len(new.text) == 2:
                data.add(new.text)
            elif new.text[2] == '(':
                data.add(new.text[:2])
            elif len(new.text) == 3:
                data.add(new.text)
            elif new.text[3] == '(':
                data.add(new.text[:3])
            elif len(new.text) == 4:
                data.add(new.text)
            elif new.text[4] == '(':
                data.add(new.text[:4])
            else:
                continue
        print(str(index) +'/5511    ' + str(index/5511*100)+'%')
    data = list(data)
    datas = [''] * 230000
    index1 = 0
    for index2 in data:
        datas[index1] = index2 + '/NNG'
        index1 += 1

    return datas
dics = daum_list()
f = open("Name.txt", 'w')
for dic in dics:
    data = "%s\n" %dic
    f.write(data)
f.close()