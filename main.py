import json
import googlemaps

# Add your Geocode API key obtained in https://console.cloud.google.com
gmaps = googlemaps.Client(key='GEOCODE API KEY')

input_file = 'data.json' # relative path to entry dataset, see sample for current json structure
output_file = 'output.json' # relative path to output dataset

data = None

with open(input_file) as f:
    data = json.loads(f.read())

count = 0

for item in data:
    print(f'[{(count/len(data))*100:.2f}%]', end=" - ")

    location = f"{item['city']}, {item['state']}, {item['country']}" # item.city, item.state, item.country, change this accordingly

    print(location, end=" -> ")

    loc = gmaps.geocode(location) # location gets fed in here

    item['latitude'] = loc[0]['geometry']['location']['lat'] # item.latitude gets set as int with results of '[result.geometry.location.lat]'
    item['longitude'] = loc[0]['geometry']['location']['lng'] # item.longitude gets set as int with results of '[result.geometry.location.lng]'

    print(f"{item['latitude']}, {item['longitude']}")

    count += 1

with open(output_file, 'w') as f:
    json.dump(data, f, indent = 2) # You can remove indent if you don't intend to prettify your json
    print('\n** Geocodes added to the dataset **')
