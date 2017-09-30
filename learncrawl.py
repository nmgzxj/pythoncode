# coding: utf-8
from urllib import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages

    html = urlopen("http://www.enwikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html)

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            print(link.attrs['href'])
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print newPage
                pages.add(newPage)
                getLinks(newPage)
getLinks("")