import codecs
import urllib.request as req
from bs4 import BeautifulSoup
from konlpy.tag import Okt

def search(page):
    data = [[]for _ in range(len(page))]
    for index in range(len(page)):
        res = req.urlopen(page[index])
        soup = BeautifulSoup(res, "html.parser")
        text = soup.select_one("#contents > div.article_view > div.article_txt").text
        okt = Okt()
        word_dic = {}
        lines = text.split("\n")
        for line in lines:
            malist = okt.pos(line)
            for word in malist:
                if word[1] == "Noun":
                    if not (word[0] in word_dic):
                        word_dic[word[0]] = 0
                    word_dic[word[0]] += 1

        keys = sorted(word_dic.items(),key=lambda x:x[1],reverse=True)
        for word, count in keys[:10]:
            data[index].append("{0}".format(word))

    return data
