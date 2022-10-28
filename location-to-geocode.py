from geopy.geocoders import Nominatim


def get_geocode(location_name):
    geolocator = Nominatim(user_agent="myGeocoder")
    
    address_string = "bangkle"
    location = geolocator.geocode(address_string)

    return location.raw