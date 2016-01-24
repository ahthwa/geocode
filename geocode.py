#!/usr/bin/python
#-*- coding:utf-8 -*-

import urllib
import json
import xml.etree.ElementTree as ET

def geocode(addr):
    """
    >>> geocode("서울특별시 중구 퇴계로 100")
    {u'lat': 37.5602013, u'lng': 126.9829327}
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
    daum_key = ""
    url = "http://apis.daum.net/local/geo/transcoord?apikey=%s&x=%s&y=%s&fromCoord=KTM&toCoord=WGS84&output=json"
    result = json.loads(urllib.urlopen(url %(daum_key, x, y)).read())
    if ('y' not in result or 'x' not in result):
        result = {'x':'', 'y':''}
    else:
        result['x'] = "%f" %(result['x'])
        result['y'] = "%f" %(result['y'])
    return result

def search(name, naver_searchapi_key):
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


