import re
import json
import requests

response = requests.get('http://nyctmc.org/')
text = response.content

latlngs = re.findall('([\d.-]+)", "([\d.-]+)', text)
streets = re.findall('c_html\d+ = "([\d\w\s(?@)(?\-)(?.)]+)', text)
images = re.findall('window.open\("([\w\_.\?\=\d]+)"', text)
latlng = []
for tup in latlngs:
    latlng.append((float(tup[0]), float(tup[1])))

location = {}
for i in range(len(latlng)):
    try:
        location["location"+str(i)] = [latlng[i][0], latlng[i][1], streets[i], "nyctmc.org/"+images[i]]
    except Exception:
        location["location"+str(i)] = "No Street Name Found?"
f.close()

location = json.dumps(location)
f = open('location.txt', 'w+')
f.write(location)
f.close()