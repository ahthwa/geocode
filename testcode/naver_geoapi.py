#!/usr/bin/python
#-*- coding:UTF-8 -*-

import urllib
import xml.etree.ElementTree as ET

keycode = ''

# 네이버 검색 API
# 첫번째 지도 검색 결과에서 주소와 좌표를 꺼낸다.

def getFirstAddressCoord(query):
    url='http://openapi.naver.com/search?key=%s&query=%s&target=local&start=1&display=1'

    f = urllib.urlopen(url %(keycode, urllib.quote(query)))
    xmldata = f.read()

    tree = ET.fromstring(xmldata)

    channel = tree.find("channel")
    items = channel.getiterator("item")

    address = ''
    mapx = ''
    mapy = ''

    for i in items:
        address = i.find("address").text
        mapx =  i.find("mapx").text
        mapy = i.find("mapy").text
        break
    return {"query":query, "address":address, "mapx":mapx, "mapy":mapy}
    #, "addrdetail":addrdetail}

#print getFirstAddressCoord("모아미래도7단지아파트")["address"]
print getFirstAddressCoord("홍능갈비집")["address"]

from lxml import html
import requests

# 네이버 지도 API
# 주소에서 위도/경도 좌표 가져오기
def getLonLatOfAddr(addr):
    apikey = ''
    url = 'http://openapi.map.naver.com/api/geocode.php?key=%s&encoding=utf-8&coord=latlng&query=%s'
    url = 'http://openapi.map.naver.com/api/geocode?key=c72ca21dd8c9bcc21d636be383f77b18&encoding=utf-8&coord=latlng&output=json&query=서울특별시%20중구%20퇴계로%20100%20(회현동%202가)'

    root = html.parse(url % (apikey, addr))
    lon, lat = root.xpath('//point/x/text()')[0], root.xpath('//point/y/text()')[0]
    return {"address":addr, "lon":lon, "lat":lat}

'''
getLonLatOfAddr("서울특별시 동대문구 청량리동 520-14") # OK
getLonLatOfAddr("서울특별시 중구 퇴계로 100 (회현동2가)") # FAIL
getLonLatOfAddr("서울특별시 중구 퇴계로 100") # FAIL
getLonLatOfAddr("서울특별시 중구 회현동2가") # OK

print getLonLatOfAddr("서울특별시 중구 회현동2가")["lon"]
print getLonLatOfAddr("서울특별시 중구 회현동2가")["lat"]

'http://openapi.naver.com/map/getStaticMap?parameters'
'https://openapi.map.naver.com/openapi/naverMap.naver?ver=2.0&key=&'
'http://openapi.naver.com/map/getStaticMap?version=1.0&crs=EPSG:4326&center=127.1141382,37.3599968&amp;level=3&w=320&h=320&maptype=default&key=발급키&uri=등록디렉토리'
'''
