import pandas as pd
import folium

# Load data
data = pd.read_csv('data/UNESCO_SDG_Feb2023_.csv')

# Filter data to include only schools
schools = data[data['Target'] == 'Education 2030 FFA']

# Create a map centered at (0, 0)
m = folium.Map(location=[0, 0], zoom_start=2)

# Add markers for each school
# for index, row in schools.iterrows():
#     lat = row['Latitude']
#     lon = row['Longitude']
#     name = row['Institution_Name']
#     folium.Marker([lat, lon], popup=name).add_to(m)

# # Save the map as an HTML file
# m.save('schools_map.html')
