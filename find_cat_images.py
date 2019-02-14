# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a python script file in order to find puppet cats images from weibo search.
"""


import urllib.request
import re

full_imglist =[]
def getHtml(url):   
    page = urllib.request.urlopen(url) ### this function is aimed to read html source code, be careful py2.7 and py3.5+ 
    html = page.read().decode('utf-8')
    return html

##def getImg(html):
##    reg = 'src="(.+?\.jpg)" action-data='
##    imgre = re.compile(reg)
##    imglist = re.findall(imgre, html)
##    x = 0
##    for imgurl in imglist:
##        urllib.request.urlretrieve(('https:'+imgurl), '%s.jpg' % x)
##        x+=1
##        full_imglist.append('https:'+imgurl)
##    return full_imglist
#    
#
#html = getHtml("https://s.weibo.com/weibo?q=%E5%B8%83%E5%81%B6%E7%8C%AB&Refer=index")
#
##results=getImg(html)
#
#
#reg = 'src="(.+?\.jpg)" action-data='
#imgre = re.compile(reg)
#imglist = re.findall(imgre, html)
#x = 0
#for imgurl in imglist:
#    urllib.request.urlretrieve(('https:'+imgurl), '%s.jpg' % x)
#    x+=1
#    full_imglist.append('https:'+imgurl)


for i in range(50):  ### generally weibo search only display 50 pages recently, if you want more images, should try it after some days
    i=i+1
    if i == 1 :
        html = getHtml("https://s.weibo.com/weibo?q=%E5%B8%83%E5%81%B6%E7%8C%AB&Refer=index")
        
        reg = 'src="(.+?\.jpg)" action-data='
        imgre = re.compile(reg)
        imglist = re.findall(imgre, html)
        x = 0
        for imgurl in imglist:
            urllib.request.urlretrieve(('https:'+imgurl), 'Puppet_cat_%s.jpg' % x)  ### save as puppet cat and its number
            x+=1
            full_imglist.append('https:'+imgurl)
    else:
        new_html = "https://s.weibo.com/weibo?q=%E5%B8%83%E5%81%B6%E7%8C%AB&Refer=index&page=" + str(i)
        
        html = getHtml(new_html)
        
        reg = 'src="(.+?\.jpg)" action-data='
        imgre = re.compile(reg)
        imglist = re.findall(imgre, html)
        for imgurl in imglist:
            urllib.request.urlretrieve(('https:'+imgurl), 'Puppet_cat_%s.jpg' % x) ### save as puppet cat and its number
            x+=1
            full_imglist.append('https:'+imgurl)      ### also obtain its corresponding url for other users 