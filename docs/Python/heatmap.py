import folium

# Create a map object
map_object = folium.Map(location=[37.7749, -122.4194], zoom_start=12)

# Display the map
map_object.save('map.html')
