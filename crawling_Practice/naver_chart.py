import re
import requests

re.findall('<span class="ah_k">(.*)</span>',requests.get('http://naver.com').text)[20:]