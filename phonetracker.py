import phonenumbers
from phonenumbers import geocoder
#from test import number
import folium

Key = "281820afaa4f450b99288c2f7d1f3af5"


number = input("Enter your Phone Number with CountryCode :")
check_number = phonenumbers.parse(number)
num_location = geocoder.description_for_number(check_number,"en")
print(num_location)

from phonenumbers import carrier
carrier_name = phonenumbers.parse(number)
print(carrier.name_for_number(carrier_name, "en"))


from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)

query = str(num_location)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

map_loc = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=num_location).add_to(map_loc)
map_loc.save("mylocation.html")