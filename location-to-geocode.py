from geopy.geocoders import Nominatim


def get_geocode(location_name):
    geolocator = Nominatim(user_agent="myGeocoder")
    
    address_string = location_name
    location = geolocator.geocode(address_string)

    if location != None:
        return location.raw
    else:
        return 404

print(get_geocode("bangkle blora"))