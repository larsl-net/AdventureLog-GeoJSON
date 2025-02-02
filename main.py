import requests, json, osm2geojson

result = requests.post(
    "https://overpass-api.de/api/interpreter",
    data='[out:json];relation["boundary"="administrative"]["admin_level"="4"]["name"="Bayern"];out body;way(r);(._;>;);out geom;'
)

geojson = osm2geojson.json2geojson(result.json())


if result.status_code != 200:
    print("Error")
else:
    with open('data.json', 'w') as f:
        json.dump(geojson, f)

# result = api.get('[out:json];relation["boundary"="administrative"]["admin_level"="4"]["name"="Bayern"];out body;way(r);(._;>;);out skel qt;', verbosity='skel qt')


# print(result)

# with open("./test.geo.json",mode="w") as f:
#   geojson.dump(result,f)

# [out:json];
# relation["boundary"="administrative"]["admin_level"="4"]["name"="Bayern"];
# out geom;
