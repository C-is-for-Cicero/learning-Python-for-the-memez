import pandas
import folium


data = pandas.read_csv("Volcanoes.txt")
print(data["NAME"])

lat = data["LAT"]
lon = data["LON"]
elevation = data["ELEV"]


def color_function(el):
    if el < 1000:
        return 'green'
    elif 1000 <= el < 3000:
        return 'orange'
    else:
        return 'red'


map_1 = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fgv=folium.FeatureGroup("Volcanoes")
for la, ln, el in zip(lat, lon, elevation):
    fgv.add_child(folium.CircleMarker(location=[la, ln],radius=6, popup=str(el)+"m", color=color_function(el)))

fgp=folium.FeatureGroup("Population")

fgp.add_child(folium.GeoJson(data=(open("world.json","r",encoding="utf-8-sig").read()),
                            style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
                                                     else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))


map_1.add_child(fgv)
map_1.add_child(fgp)
map_1.add_child(folium.LayerControl())
map_1.save("map.html")
