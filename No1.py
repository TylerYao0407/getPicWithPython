from __future__ import division
import urllib
import re
import os

url = "http://desk.zol.com.cn/bizhi/6960_86589_2.html"

def getHtml(url):
        page = urllib.urlopen(url)
        html = page.read()
        return html

def getPic(html):
        picreg = r'src=".*?\.jpg"'
        repic = re.compile('src="(http:.*?\.jpg)"')
        piclist = repic.findall(html)
        piclistlen = len(piclist)
        print piclistlen
        x = 0
        for pic in piclist:
            urllib.urlretrieve(pic, "%s.jpg" % x)
            x += 1
            c = (x/piclistlen)*100
            print ("downloading---- %d " % c + "%")
getPic(getHtml(url))
