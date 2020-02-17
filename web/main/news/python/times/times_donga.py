import requests
import codecs
import urllib.request as req
from bs4 import BeautifulSoup
from konlpy.tag import Kkma

def search(page):
    data = [[]for _ in range(len(page))]
    for index in range(len(page)):
        res = req.urlopen(page[index])
        soup = BeautifulSoup(res, "html.parser")
        text = soup.select("#contents > div.article_view > div.article_txt")
        text = " ".join(map(lambda x: str(x), text))
        kkma = Kkma()
        word_dic = {}
        words = kkma.pos(text)
        for word in words:
            if (word[1] == "NNP" or word[1] == "NN" or word[1] == "NNG") and len(word[0]) > 1:
                if not (word[0] in word_dic):
                    word_dic[word[0]] = 0
                word_dic[word[0]] += 1
            
        keys = sorted(word_dic.items(),key=lambda x:x[1],reverse=True)

        for word, count in keys[:10]:
            data[index].append("{0}".format(word))

    return data
