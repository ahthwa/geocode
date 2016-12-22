#!/usr/bin/python

import os
import sys
import urllib.request
import json

naver_client_id = 'YOUR_CLIENT_ID'
naver_client_secret = 'YOUR_CLIENT_SECRET'

def _request(url, ext_header = {}):
    request = urllib.request.Request(url)
    for k, v in ext_header.items():
        request.add_header(k, v)
    response = urllib.request.urlopen(request)
    return response

def _select_element(a_dict, element_name, element_buffer):
    if (element_name in a_dict):
        element_buffer.append(a_dict[element_name])
    return a_dict

def naver_geocode(addr):
    """
    result: (lat, lng)
    >>> naver_geocode("서울특별시 중구 퇴계로 100")
    (37.5602997, 126.9829401)
    >>> naver_geocode("서울특별시 중구 퇴계로 101")
    (37.5608791, 126.9830887)
    >>> naver_geocode("서울특별시 중구 퇴계로 101, 건물전체")
    (37.5608791, 126.9830887)
    """

    encText = urllib.parse.quote(addr)
    url = "https://openapi.naver.com/v1/map/geocode?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/map/geocode.xml?query=" + encText # xml 결과
    response = _request(url, {"X-Naver-Client-Id":naver_client_id, "X-Naver-Client-Secret":naver_client_secret})
    rescode = response.getcode()

    coord = []
    if(rescode==200):
        response_body = response.read().decode('utf-8')
        json.loads(response_body, object_hook = lambda x: _select_element(x, 'point', coord))
        if (len(coord) < 1):
            return None
        return [(c['y'], c['x']) for c in coord][0]
    else:
        return rescode

def naver_reverse_geocode(lat, lng):
    """
    >>> naver_reverse_geocode(37.5602997, 126.9829401)
    '서울특별시 중구 퇴계로 100 스테이트타워 남산'
    """
    url = "https://openapi.naver.com/v1/map/reversegeocode?query=%f,%f" %(lng,lat)
    response = _request(url, {"X-Naver-Client-Id":naver_client_id, "X-Naver-Client-Secret":naver_client_secret})
    rescode = response.getcode()

    addr = []
    if (rescode == 200):
        response_body = response.read().decode('utf-8')
        json_body = json.loads(response_body)
        for i in json_body['result']['items']:
            if i['isRoadAddress'] == True:
                addr.append(i['address'])
        if (len(addr) < 1):
            return None
        else:
            return addr[0]
    else:
        return rescode

    return

def naver_geo_search(query):
    """
    >>> naver_geo_search("스타벅스 남산스테이트점")
    (37.5602997, 126.9829401)
    """
    encText = urllib.parse.quote(query)
    url = "https://openapi.naver.com/v1/search/local.json?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/local.xml?query=" + encText # xml 결과
    response = _request(url, {"X-Naver-Client-Id":naver_client_id, "X-Naver-Client-Secret":naver_client_secret})
    rescode = response.getcode()

    roadAddr = []
    if(rescode==200):
        response_body = response.read().decode('utf-8')
        json.loads(response_body, object_hook = lambda x: _select_element(x, 'roadAddress', roadAddr))
        if (len(roadAddr) < 1):
            return None
        return naver_geocode(roadAddr[0])
    else:
        return rescode

def google_geocode(addr):
    """
    >>> google_geocode("서울특별시 중구 퇴계로 100")
    (37.5602013, 126.9829327)
    >>> google_geocode("서울특별시 중구 퇴계로 101")
    (37.5608244, 126.9830929)
    """

    encText = urllib.parse.quote(addr)
    url = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&language=ko&address=%s" %(encText)

    response = _request(url)
    rescode = response.getcode()

    results = []

    def _decode_dict(a_dict):
        try: results.append(a_dict["location"])
        except KeyError: pass
        return a_dict

    if(rescode==200):
        response_body = response.read().decode('utf-8')
        json.loads(response_body, object_hook = lambda x: _select_element(x, 'location', results))
        if (len(results) < 1):
            return None
        else:
            return [(c['lat'], c['lng']) for c in results][0]
    else:
        return rescode

if "__main__" == __name__:
    import doctest
    doctest.testmod(verbose=True)


