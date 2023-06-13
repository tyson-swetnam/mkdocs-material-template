import folium
import matplotlib.pyplot as plt
from io import BytesIO

# Create a map object using Folium
map_object = folium.Map(location=[37.7749, -122.4194], zoom_start=12)

# Add a marker to the map
folium.Marker(location=[37.7749, -122.4194], popup='San Francisco').add_to(map_object)

# Save the map as HTML
map_html = map_object._repr_html_()

# Display the map using Matplotlib
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_axis_off()
png_image = BytesIO()
map_object.save(png_image, close_file=False)
plt.imshow(plt.imread(png_image))
plt.show()
