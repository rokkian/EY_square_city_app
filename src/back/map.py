import folium
from geopy.geocoders import Nominatim

def get_nearby_locations(user_location):
    geolocator = Nominatim(user_agent="my-application")
    location = geolocator.geocode(user_location)
    
    # Get the latitude and longitude of the user's location
    user_lat = location.latitude
    user_lon = location.longitude
    
    # Create a map centered around the user's location
    map_center = [user_lat, user_lon]
    map_object = folium.Map(location=map_center, zoom_start=15)
    
    # Add a marker for the user's location on the map
    folium.Marker(location=map_center, popup="User Location").add_to(map_object)
    
    # Search for nearby locations using the user's coordinates
    nearby_locations = geolocator.reverse([user_lat, user_lon], exactly_one=False)
    
    # Add markers for the nearby locations on the map
    for nearby_location in nearby_locations:
        location_name = nearby_location.address
        location_lat = nearby_location.latitude
        location_lon = nearby_location.longitude
        folium.Marker(location=[location_lat, location_lon], popup=location_name).add_to(map_object)
    
    # Save the map as an HTML file
    map_object.save("map.html")
    print("Map saved as map.html")

# Provide the user's location as input
user_location = "Your Location"

# Call the function to get nearby locations and generate the map
get_nearby_locations(user_location)
