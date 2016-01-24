#!/usr/bin/python
# -*- coding:utf-8 -*-

from lxml import html
import requests
import json

def getLonLatOfAddr(addr):
    url = 'http://maps.googleapis.com/maps/api/geocode/json?sensor=false&language=ko&address=%s'

    googlemap_response = '{\
        "results" : [\
        {\
            "address_components" : [ { "long_name" : "100", "short_name" : "100", "types" : [ "premise", "political" ] },\
            { "long_name" : "퇴계로", "short_name" : "퇴계로", "types" : [ "sublocality_level_4", "sublocality", "political" ] },\
            { "long_name" : "중구", "short_name" : "중구", "types" : [ "sublocality_level_1", "sublocality", "political" ] },\
            { "long_name" : "서울특별시", "short_name" : "서울특별시", "types" : [ "locality", "political" ] },\
            { "long_name" : "대한민국", "short_name" : "KR", "types" : [ "country", "political" ] },\
            { "long_name" : "100-052", "short_name" : "100-052", "types" : [ "postal_code" ] }\
            ],\
                "formatted_address" : "대한민국 서울특별시 중구 퇴계로 100",\
                "geometry" : {\
                    "location" : { "lat" : 37.5602013, "lng" : 126.9829327 },\
                    "location_type" : "ROOFTOP",\
                    "viewport" : {\
                        "northeast" : { "lat" : 37.5690459, "lng" : 126.9989401 },\
                        "southwest" : { "lat" : 37.55135569999999, "lng" : 126.9669253 }\
                    }\
                },\
                "place_id" : "ChIJ0QZlMvGifDURJVTQ0eOoVaQ",\
                "types" : [ "premise", "political" ]\
        }\
        ],\
            "status" : "OK"\
    }'
    results = []

    def _decode_dict(a_dict):
        try: results.append(a_dict["location"])
        except KeyError: pass
        return a_dict

    json.loads(googlemap_response, object_hook = _decode_dict)
    return results

if __name__ == '__main__':
    latlon = getLonLatOfAddr("테스트")
    print latlon[0]['lat']
    print latlon[0]['lng']
    print latlon
