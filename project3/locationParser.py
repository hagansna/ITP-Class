import re
import json

f = open('cameraLocations.txt', 'r+')
file = f.read()

latlngs = re.findall('([\d.-]+)", "([\d.-]+)', file)
streets = re.findall('c_html\d+ = "([\d\w\s(?@)(?\-)(?.)]+)', file)
images = re.findall('window.open\("([\w\_.\?\=\d]+)"', file)
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