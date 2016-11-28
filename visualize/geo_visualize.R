library(ggplot2)
library(data.table)
library(ggmap)
 
geodata = fread('shopdata/geodata.fin.tsv', header=F, sep = '\t')
names(geodata) = c('type', 'no', 'area', 'name', 'addr', 'phone', 'lat', 'lng')

al1 = get_map(location = c(lat = 37.5620923, lon = 126.9810679), zoom = 10, maptype = 'roadmap', color = "bw")
ggmap(al1) + geom_point(aes(x = lng, y = lat, size = 1500, color = as.factor(type)), alpha=0.3, data = geodata)
