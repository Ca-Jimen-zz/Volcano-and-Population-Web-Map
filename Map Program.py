import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

#Color scheme for volcanoes
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start = 6, tiles = 'Stamen Terrain')

#Create feature groups for Volcanoes and Population
fgv = folium.FeatureGroup('Volcanoes')
fgp = folium.FeatureGroup('Population')

#This loop adds the location/color of volcanoes on map
for la, lo, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[la, lo],radius=6, popup=str(el)+' m', fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))

#Color scheme for population
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor': 'green' if x ['properties']['POP2005'] < 10000000 
else 'orange' if x['properties']['POP2005'] < 100000000  else 'red'}))

#adds volcanoes and populations to map
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save('Map1.html')