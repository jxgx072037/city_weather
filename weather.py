# -*- coding: utf-8 -*-
import urllib2
from city import city
import json

cityname=raw_input('你想查询哪个城市的天气：')
citycode=city.get(cityname)
if citycode:
    web='http://www.weather.com.cn/data/cityinfo/%s.html'%(citycode)
    content=urllib2.urlopen(web).read()
    data=json.loads(content)
    wea=data['weatherinfo']
    if citycode==wea['cityid']:
        temph=wea['temp1']
        templ=wea['temp2']
        w=wea['weather']
        print 'The weather is %s, %s~%s'%(w,templ,temph)
        
    
