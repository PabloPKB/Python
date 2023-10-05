import phonenumbers
import folium
from my_number import number
from phonenumbers import geocoder

Key = 'eb78383283344751a27ad977fb44c2f3'

samNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(samNumber, "pt")
print(yourLocation)

# get service provider
from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "pt"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)
print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng],popup=yourLocation).add_to((myMap))

# save map in html file
myMap.save("myLocation.html")