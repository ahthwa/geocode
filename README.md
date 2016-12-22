# Geocode Package

주소, 검색어에 해당하는 지리 좌표를 구하는 python package  
naver 지도 API, 검색 API, google map API wrapper

## API

### naver\_geocode

naver 지도 API를 통해 주소에 대한 위도 경도 좌표를 구한다.

```python
    >>> import geocode
    >>> geocode.naver_geocode("서울특별시 중구 퇴계로 100")
    (37.5602997, 126.9829401)
```

### naver\_reverse\_geocode

naver 지도 API를 통해 위도, 경도 좌표에 대한 주소를 구한다.

```python
    >>> import geocode
    >>> goecode.naver_reverse_geocode(37.5602997, 126.9829401)
    '서울특별시 중구 퇴계로 100 스테이트타워 남산'
```

### naver\_geo\_search

naver 검색 API를 통해 지역 검색 첫번째 결과의 위도, 경도 좌표를 구한다.

```python
    >>> import geocode
    >>> geocode.naver_geo_search("스타벅스 남산스테이트점", API_KEY)
    (37.5602997, 126.9829401)
```

### google\_geocode

google map API를 통해 주소에 대한 위도 경도 좌표를 구한다.

```python
    >>> import geocode
    >>> geocode.google_geocode("서울특별시 중구 퇴계로 100")
    (37.5602013, 126.9829327)
```

## Reference

네이버 API, 구글 API의 위치 정확도가 주소에 따라 달라서 네이버 API를 default로, 네이버 API의 결과가 없는 경우 구글 API를 사용함

* [네이버 지도 API](https://developers.naver.com/docs/map/overview)
* [네이버 검색 API - 지역](https://developers.naver.com/docs/search/local)
* [Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding/intro)  
* RgoogleMap
```
> library(RgoogleMaps)
> getGeoCode("서울특별시 중구 퇴계로 101, 건물전체")
      lat       lon
       37.56097 126.99460
```
