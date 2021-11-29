import folium

map = folium.Map(location=[14.586250, 120.999935], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My map")
fg.add_child(folium.Marker(location=[14.586250, 120.999935], popup="marker pointer", icon=folium.Icon(color="blue")))
map.add_child(fg)

map.save("pandacan_bbac.html")