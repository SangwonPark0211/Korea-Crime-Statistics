import urllib
from urllib import parse
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

naver_url = 'https://dict.naver.com/name-to-roman/translation/?query='
name_url = naver_url + urllib.parse.quote("경북포항남구")

req = Request(name_url)
res = urlopen(req)

html = res.read().decode('utf-8')
bs = BeautifulSoup(html, 'html.parser')
name_tags = bs.select('#container > div > table > tbody > tr > td > a')
names = [name_tag.text for name_tag in name_tags]

print(names)