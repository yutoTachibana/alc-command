#!/usr/bin/python
# -*- coding: utf_8 -*-

import mechanize, sys, re
from BeautifulSoup import BeautifulSoup

if (len(sys.argv) != 2): quit("検索ワードを指定してください")

print "検索ワード:",sys.argv[1],"\n"

BASE_URL = "http://eow.alc.co.jp/"+sys.argv[1]+"/UTF-8/?ref=sa"
soup = BeautifulSoup(mechanize.Browser().open(BASE_URL).get_data())
li = soup.find(id="resultsList").find("li")

if (not li): quit("見つかりませんでした")

div = li.find("div")
if (div.find("ul") and div.find("ul")['class'] == "ul_je"):
    for hit in div.findAll("li"): print re.compile(r'<.*?>').sub('', unicode(hit))
elif (div.find("span", {"class":"wordclass"})):
    div = unicode(li.find("span", {"class":"midashi"}))+"\n"+unicode(div)
    div = re.compile(r'</span><ol>|</li>').sub("\n", unicode(div))
    div = re.compile(r'<li>').sub("  ", unicode(div))
    print re.compile(r'<.*?>').sub('', unicode(div))
elif (soup.find(id="resultsList").find("ul")):
    div = re.compile(r"\n").sub('', unicode(soup.find(id="resultsList").find("ul")))
    div = re.compile(r"</span>").sub("\n", unicode(div))
    print re.compile(r'<.*?>').sub('', unicode(div))
else: quit("見つかりませんでした")
