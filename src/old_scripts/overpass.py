import overpy
api = overpy.Overpass()

quick_c = [43.947300096957186, -79.7710501044725, 43.58421719106671, -78.98435889455229]
#quick_c is quick coordinate, paste in two coordinates into the list above and it will be re-ordered for OSM as the bounding box
if quick_c[2] < quick_c[0]:
    t = quick_c[0]
    quick_c[0] = quick_c[2]
    quick_c[2] = t
if quick_c[3] < quick_c[1]:
    t = quick_c[1]
    quick_c[1] = quick_c[3]
    quick_c[3] = t

print(quick_c)

query = f"""
    [out:json];
    area[name="Markham"];
    node({quick_c[0]},{quick_c[1]},{quick_c[2]},{quick_c[3]})(area)["amenity"="restaurant"];
    out;
    """

print(query)
result = api.query(query)
#result = api.query("node(50.745,7.17,50.75,7.18);out;")
with open("output.txt", "w", encoding='utf-8') as f:
    for x in result.nodes:
        #print(x.__dict__)
        if 'name' in x.tags:
            f.write(f"{x.lat},{x.lon} {x.tags['name']}\n")
            #print(f"{x.lat},{x.lon} {x.tags['name']}")