#!/usr/bin/python
#-*- coding:utf-8 -*-

import urllib
import json
import xml.etree.ElementTree as ET

naver_geocode_key = ''
naver_searchapi_key = ''
daum_key = ''

def geocode(addr):
    return naver_geocode(addr)

def naver_geocode(addr):
    """
    >>> naver_geocode("서울특별시 중구 퇴계로 100")
    {u'lat': 37.5602997, u'lng': 126.9829401}
    >>> naver_geocode("서울특별시 중구 퇴계로 101")
    {u'lat': 37.5608791, u'lng': 126.9830887}
    >>> naver_geocode("서울특별시 중구 퇴계로 101, 건물전체")
    {u'lat': 37.5608791, u'lng': 126.9830887}
    """
    url = 'http://openapi.map.naver.com/api/geocode?key=%s&encoding=utf-8&coord=latlng&output=json&query=%s'

    resp = urllib.urlopen(url %(naver_geocode_key, addr)).read()
    results = []

    def _decode_dict(a_dict):
        try: results.append(a_dict["point"])
        except KeyError: pass
        return a_dict

    json.loads(resp, object_hook = _decode_dict)
    lat = ''
    lng = ''
    if (len(results) >= 1):
        lat = results[0]['y']
        lng = results[0]['x']
    return {u"lat":lat, u"lng":lng}

def google_geocode(addr):
    """
    >>> google_geocode("서울특별시 중구 퇴계로 100")
    {u'lat': 37.5602013, u'lng': 126.9829327}
    >>> google_geocode("서울특별시 중구 퇴계로 101")
    {u'lat': 37.5608244, u'lng': 126.9830929}
    >>> google_geocode("경기도 동두천시 싸리말로 미2사단 캠프케이시 PX Mall")
    {u'lat': 37.9179091, u'lng': 127.0642171}
    """

    url = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&language=ko&address=%s"
    resp = urllib.urlopen(url %(addr)).read()

    results = []

    def _decode_dict(a_dict):
        try: results.append(a_dict["location"])
        except KeyError: pass
        return a_dict

    json.loads(resp, object_hook = _decode_dict)
    if (len(results) < 1):
        return {"lat":"", "lng":""}
    else:
        return results[0]

def KTMtoWGS(x, y):
    """
    >>> KTMtoWGS("315637", "554292")
    {u'y': '37.587033', u'x': '127.042563'}
    """
    url = "http://apis.daum.net/local/geo/transcoord?apikey=%s&x=%s&y=%s&fromCoord=KTM&toCoord=WGS84&output=json"
    result = json.loads(urllib.urlopen(url %(daum_key, x, y)).read())
    if ('y' not in result or 'x' not in result):
        result = {'x':'', 'y':''}
    else:
        result['x'] = "%f" %(result['x'])
        result['y'] = "%f" %(result['y'])
    return result

def search(name):
    """
    >>> search("스타벅스 남산스테이트점")
    {u'lat': 37.560468, u'lng': 126.983027}
    """
    url='http://openapi.naver.com/search?key=%s&query=%s&target=local&start=1&display=1'

    f = urllib.urlopen(url %(naver_searchapi_key, urllib.quote(name)))
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
    latlng = KTMtoWGS(mapx, mapy)
    lat = float(latlng.get('y', 0.0))
    lng = float(latlng.get('x', 0.0))
    return {u"lat":lat, u"lng":lng}

if "__main__" == __name__:
    import doctest
    doctest.testmod(verbose=True)


