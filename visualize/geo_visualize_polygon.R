library(geosphere)
  
## 위치로부터 반경 radius, n_angles 각형의 좌표 만들기 함수
makeCircle <- function(x, radius=1000, n_angles=30, index=NULL, type=NULL) {
  # Creation n_angles points
  # center : x , distance : radius(meter)
  # default : 1km, 20angles
  # x = c("lon", "lat", "index", "type")
   
  index = x[3]
  type = x[4]
  resul <- do.call("rbind", lapply(seq(0,360,360/n_angles), function(bearing) {
    res <- destPoint(p = x[1:2], b = bearing, d = radius)
    rownames(res) <- NULL
    return(data.frame(res))
  }))
  resul$index <- index
  resul$type <-type
  return(resul)
}
 
##############
 
## 여러 지점에서의 좌표 데이터 만들기 함수
circleData <- function(data, n_angles=30, radius=1000){
  # names(data) = c("lon", "lat", "index", "type")
  result <- do.call("rbind", apply(data,1, function(x) makeCircle(x,n_angles=n_angles, radius=radius))) 
  return(result)
}
 
geodata = fread('shodata/geodata.fin.tsv', header=F, sep = '\t')
names(geodata) = c('type', 'no', 'area', 'name', 'addr', 'phone', 'lat', 'lng')
  
al1 = get_map(location = c(lat = 37.5620923, lon = 126.9810679), zoom = 10, maptype = 'roadmap', color = "bw")
 
## circle 데이터 만들기
new.geodata <- geodata[, .(lon=lng, lat=lat,  index=paste(type,no,sep = ""), type=type)]
geodata_circle <-circleData(new.geodata, n_angles=30, radius=1000) ## 30각형, 반경 1km
 
## 그리기
ggmap(al1) + geom_polygon(data = geodata_circle, aes(x=lon, y=lat, group=index, fill=type), alpha=0.2)
