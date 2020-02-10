
import codecs
import urllib.request as req
from bs4 import BeautifulSoup
from konlpy.tag import Okt

def search(page):
    data = [[] for _ in range(len(page))]
    for index in range(len(page)):
        res = req.urlopen(page[index])
        soup = BeautifulSoup(res, "html.parser")
        text = str(soup.select("#article_story"))
        okt = Okt()
        word_dic = {}
        for line in text:
            malist = okt.pos(line)
            if malist == []:
                continue
            if malist[0][1] == "Noun":
                if not (malist[0][0] in word_dic):
                    word_dic[malist[0][0]] = 0
                word_dic[malist[0][0]] += 1
        keys = sorted(word_dic.items(),key=lambda x:x[1],reverse=True)
        for word, count in keys[:10]:
            data[index].append("{0}".format(word))

    return data
