#!/usr/bin/python
#-*- coding:utf-8 -*-

import urllib

def exec_google_api(addr):
    url = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&language=ko&address=%"
    # ex: 서울특별시 중구 퇴계로 100"
    return urllib.urlopen(url %(addr))
