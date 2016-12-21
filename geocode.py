#!/usr/bin/python

import os
import sys
import urllib.request
import json

#client_id = "YOUR_CLIENT_ID"
#client_secret = "YOUR_CLIENT_SECRET"
naver_client_id = 'BznHFaLzhxwNQxjOX22m'
naver_client_secret = 'pVvR5ZG_yl'

def _request(url, ext_header, resp_success_callback):
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",naver_client_id)
    request.add_header("X-Naver-Client-Secret",naver_client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read().decode('utf-8')
        return resp_success_callback(response_body)
    else:
        return None

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
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",naver_client_id)
    request.add_header("X-Naver-Client-Secret",naver_client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    coord = []
    def _decode_point(a_dict):
        try: coord.append((a_dict['y'], a_dict['x']))
        except KeyError: pass
        return a_dict

    if(rescode==200):
        response_body = response.read().decode('utf-8')
        json.loads(response_body, object_hook = _decode_point)
        return coord[0]
    else:
        return rescode

def naver_geo_search(query):
    """
    >>> naver_geo_search("스타벅스 남산스테이트점")
    (37.5602997, 126.9829401)
    """
    encText = urllib.parse.quote(query)
    url = "https://openapi.naver.com/v1/search/local.json?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/local.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",naver_client_id)
    request.add_header("X-Naver-Client-Secret",naver_client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    roadAddr = []
    def _decode_roadAddr(a_dict):
        try: roadAddr.append(a_dict['roadAddress'])
        except KeyError: pass
        return a_dict

    if(rescode==200):
        response_body = response.read().decode('utf-8')
        json.loads(response_body, object_hook = _decode_roadAddr)
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

    url = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&language=ko&address=%s"
    encText = urllib.parse.quote(addr)
    request = urllib.request.Request(url %(encText))
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    results = []

    def _decode_dict(a_dict):
        try: results.append(a_dict["location"])
        except KeyError: pass
        return a_dict

    if(rescode==200):
        response_body = response.read().decode('utf-8')
        json.loads(response_body, object_hook = _decode_dict)
        if (len(results) < 1):
            return None
        else:
            return (results[0]['lat'], results[0]['lng'])
    else:
        return rescode

if "__main__" == __name__:
    import doctest
    doctest.testmod(verbose=True)


