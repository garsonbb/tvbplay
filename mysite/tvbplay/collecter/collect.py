from lxml import html
import requests as r
import urllib
import time
import re

class tvb(object):
    resultTitles = []
    resultUrls = []
    url =''
    def __init__(self,url):
        self.url = url

    def __get_video_(self,url):
        resp = r.get(url).content
        page = html.fromstring(resp)
        script = page.xpath("//*[@id='bofang_box']/script[1]")
        s = script[0].text
        s = s.replace("var player_data=","")
        s = s.replace("\\","")
        foo = eval(s)
    
        resp = r.get(foo['url']).text
        p = re.compile("url: '(.+)'")
        res = p.findall(resp)
        print(res)
        if len(res) == 0:
            return('#')
        return(res[0])

    def __get_videos(self,url):
        resp = r.get(url).content
        page = html.fromstring(resp)
        link = page.xpath("//*[@id='playlist_1']//@href")
        title = page.xpath("//*[@id='playlist_1']//a")
        n = 0
        for i in title:
            if i.text != "TVB直播": 
                self.resultUrls.append(self.__get_video_('http://www.hktvyb.com' + link[n]))
                self.resultTitles.append(i.text)
                n = n + 1
                time.sleep(1)
  
    
    def collect(self):
        self.resultTitles.clear()
        self.resultUrls.clear()
        self.__get_videos(self.url)

