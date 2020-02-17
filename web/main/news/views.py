from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .python import crawling_donga
from .python import crawling_hankyung
from .python import crawling_khan
from .python import crawling_mk
from .python import crawling_seoul
from .python import crawling_hankookilbo
from .python import daum_charts
# Create your views here.

# Create your views here.
@csrf_exempt
def main(request):
    ranking = daum_charts.daum_list()
    return render(request,'donga/main.html',{
        'ranking':ranking
    })

@csrf_exempt
def donga(request):
    if request.method == "POST":
        # 검색할 단어 들고온다.
        search=request.POST['search']
        # 크롤링 하는 것을 불러온다.
        title, page, data = crawling_donga.crawling(search)
        return render(request,'donga/donga.html',{
            'title1':title[0],
            'title2':title[1],
            'title3':title[2],
            'title4':title[3],
            'title5':title[4],
            'title6':title[5],
            'title7':title[6],
            'title8':title[7],
            'title9':title[8],
            'title10':title[9],
            'title11':title[10],
            'title12':title[11],
            'title13':title[12],
            'title14':title[13],
            'title15':title[14],
            'page1':page[0],
            'page2':page[1],
            'page3':page[2],
            'page4':page[3],
            'page5':page[4],
            'page6':page[5],
            'page7':page[6],
            'page8':page[7],
            'page9':page[8],
            'page10':page[9],
            'page11':page[10],
            'page12':page[11],
            'page13':page[12],
            'page14':page[13],
            'page15':page[14],
            'data1': data[0],
            'data2': data[1],
            'data3': data[2],
            'data4': data[3],
            'data5': data[4],
            'data6': data[5],
            'data7': data[6],
            'data8': data[7],
            'data9': data[8],
            'data10': data[9],
            'data11': data[10],
            'data12': data[11],
            'data13': data[12],
            'data14': data[13],
            'data15': data[14],
            'search':search,
            })
    else:
        return render(request,'donga/donga.html')



@csrf_exempt
def hankookilbo(request):
    if request.method == "POST":
        # 검색할 단어 들고온다.
        search=request.POST['search']
        # 크롤링 하는 것을 불러온다.
        title, page, data = crawling_hankookilbo.crawling(search)
        return render(request,'donga/hankookilbo.html',{
            'title1':title[0],
            'title2':title[1],
            'title3':title[2],
            'title4':title[3],
            'title5':title[4],
            'title6':title[5],
            'title7':title[6],
            'title8':title[7],
            'title9':title[8],
            'title10':title[9],
            'title11':title[10],
            'title12':title[11],
            'title13':title[12],
            'title14':title[13],
            'title15':title[14],
            'page1':page[0],
            'page2':page[1],
            'page3':page[2],
            'page4':page[3],
            'page5':page[4],
            'page6':page[5],
            'page7':page[6],
            'page8':page[7],
            'page9':page[8],
            'page10':page[9],
            'page11':page[10],
            'page12':page[11],
            'page13':page[12],
            'page14':page[13],
            'page15':page[14],
            'data1': data[0],
            'data2': data[1],
            'data3': data[2],
            'data4': data[3],
            'data5': data[4],
            'data6': data[5],
            'data7': data[6],
            'data8': data[7],
            'data9': data[8],
            'data10': data[9],
            'data11': data[10],
            'data12': data[11],
            'data13': data[12],
            'data14': data[13],
            'data15': data[14],
            'search':search,
            })
    else:
        return render(request,'donga/hankookilbo.html')


@csrf_exempt
def hankyung(request):
    if request.method == "POST":
        # 검색할 단어 들고온다.
        search=request.POST['search']
        # 크롤링 하는 것을 불러온다.
        title, page, data = crawling_hankyung.crawling(search)
        return render(request,'donga/hankyung.html',{
            'title1':title[0],
            'title2':title[1],
            'title3':title[2],
            'title4':title[3],
            'title5':title[4],
            'title6':title[5],
            'title7':title[6],
            'title8':title[7],
            'title9':title[8],
            'title10':title[9],
            'page1':page[0],
            'page2':page[1],
            'page3':page[2],
            'page4':page[3],
            'page5':page[4],
            'page6':page[5],
            'page7':page[6],
            'page8':page[7],
            'page9':page[8],
            'page10':page[9],
            'data1': data[0],
            'data2': data[1],
            'data3': data[2],
            'data4': data[3],
            'data5': data[4],
            'data6': data[5],
            'data7': data[6],
            'data8': data[7],
            'data9': data[8],
            'data10': data[9],
            'search':search,
            })
    else:
        return render(request,'donga/hankyung.html')


@csrf_exempt
def khan(request):
    if request.method == "POST":
        # 검색할 단어 들고온다.
        search=request.POST['search']
        # 크롤링 하는 것을 불러온다.
        title, page, data = crawling_khan.crawling(search)
        return render(request,'donga/khan.html',{
            'title1':title[0],
            'title2':title[1],
            'title3':title[2],
            'title4':title[3],
            'title5':title[4],
            'title6':title[5],
            'title7':title[6],
            'title8':title[7],
            'title9':title[8],
            'title10':title[9],
            'page1':page[0],
            'page2':page[1],
            'page3':page[2],
            'page4':page[3],
            'page5':page[4],
            'page6':page[5],
            'page7':page[6],
            'page8':page[7],
            'page9':page[8],
            'page10':page[9],
            'data1': data[0],
            'data2': data[1],
            'data3': data[2],
            'data4': data[3],
            'data5': data[4],
            'data6': data[5],
            'data7': data[6],
            'data8': data[7],
            'data9': data[8],
            'data10': data[9],
            'search':search,
            })
    else:
        return render(request,'donga/khan.html')

@csrf_exempt
def mk(request):
    if request.method == "POST":
        # 검색할 단어 들고온다.
        search=request.POST['search']
        # 크롤링 하는 것을 불러온다.
        title, page, data = crawling_mk.crawling(search)
        return render(request,'donga/mk.html',{
            'title1':title[0],
            'title2':title[1],
            'title3':title[2],
            'title4':title[3],
            'title5':title[4],
            'title6':title[5],
            'title7':title[6],
            'title8':title[7],
            'title9':title[8],
            'title10':title[9],
            'title11':title[10],
            'title12':title[11],
            'title13':title[12],
            'title14':title[13],
            'title15':title[14],
            'title16':title[15],
            'title17':title[16],
            'title18':title[17],
            'title19':title[18],
            'title20':title[19],
            'page1':page[0],
            'page2':page[1],
            'page3':page[2],
            'page4':page[3],
            'page5':page[4],
            'page6':page[5],
            'page7':page[6],
            'page8':page[7],
            'page9':page[8],
            'page10':page[9],
            'page11':page[10],
            'page12':page[11],
            'page13':page[12],
            'page14':page[13],
            'page15':page[14],
            'page16':page[15],
            'page17':page[16],
            'page18':page[17],
            'page19':page[18],
            'page20':page[19],
            'data1': data[0],
            'data2': data[1],
            'data3': data[2],
            'data4': data[3],
            'data5': data[4],
            'data6': data[5],
            'data7': data[6],
            'data8': data[7],
            'data9': data[8],
            'data10': data[9],
            'data11': data[10],
            'data12': data[11],
            'data13': data[12],
            'data14': data[13],
            'data15': data[14],
            'data16': data[15],
            'data17': data[16],
            'data18': data[17],
            'data19': data[18],
            'data20': data[19],
            'search':search,
            })
    else:
        return render(request,'donga/mk.html')

@csrf_exempt
def seoul(request):
    if request.method == "POST":
        # 검색할 단어 들고온다.
        search=request.POST['search']
        # 크롤링 하는 것을 불러온다.
        title, page, data = crawling_seoul.crawling(search)
        return render(request,'donga/seoul.html',{
            'title1':title[0],
            'title2':title[1],
            'title3':title[2],
            'title4':title[3],
            'title5':title[4],
            'title6':title[5],
            'title7':title[6],
            'title8':title[7],
            'title9':title[8],
            'title10':title[9],
            'page1':page[0],
            'page2':page[1],
            'page3':page[2],
            'page4':page[3],
            'page5':page[4],
            'page6':page[5],
            'page7':page[6],
            'page8':page[7],
            'page9':page[8],
            'page10':page[9],
            'data1': data[0],
            'data2': data[1],
            'data3': data[2],
            'data4': data[3],
            'data5': data[4],
            'data6': data[5],
            'data7': data[6],
            'data8': data[7],
            'data9': data[8],
            'data10': data[9],
            'search':search,
            })
    else:
        return render(request,'donga/seoul.html')
