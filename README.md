# Geocode Package

주소, 검색어에 해당하는 지리 좌표를 구하는 python package

## API

### geocode

주소에 해당하는 좌표를 얻는 함수


```python
    >>> import geocode
    >>> geocode.geocode("서울특별시 중구 퇴계로 100")
    {u'lat': 37.5602013, u'lng': 126.9829327}
```

### search

네이버 지역 검색 첫번째 결과의 좌표를 얻는 함수

```python
    >>> import geocode
    >>> geocode.search("스타벅스 남산스테이트점", API_KEY)
    {u'lat': 37.560468, u'lng': 126.983027}
```

## Reference

* [Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding/intro)  
도로명주소, 지번주소에 해당하는 위경도 좌표를 구함 
* [네이버 검색 API](http://developer.naver.com/wiki/pages/SrchLocal)  
상호, 점포명에 해당하는 네이버 지도검색 결과를 카텍 좌표계로 구함 
* [다음 로컬 API - 좌표계변환](http://developers.daum.net/services/apis/local/geo/transcoord)  
카텍 좌표계를 위/경도 좌표계로 변환 
* [네이버 지도 API](http://developer.naver.com/wiki/pages/JavaScript#section-JavaScript-9._EC_A3_BC_EC_86_8C_EC_A2_8C_ED_91_9C_EB_B3_80_ED_99_98)  
주소에 해당하는 위경도 좌표를 구함. 본 모듈에서는 사용하지 않음
* RgoogleMap
```
> library(RgoogleMaps)
> getGeoCode("서울특별시 중구 퇴계로 101, 건물전체")
      lat       lon
       37.56097 126.99460
```
