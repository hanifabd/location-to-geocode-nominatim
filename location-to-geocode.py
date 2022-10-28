from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="myGeocoder")

address_string = "sleman yogyakarta"
location = geolocator.geocode(address_string)

# print(location.altitude)
# print(location.latitude)
# print(location.longitude)
print(location.raw)