import overpy
api = overpy.Overpass()

quick_c = [43.87947760607178, -79.49165054311786, 43.866101913596125, -79.46284804882069]
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
    node({quick_c[0]},{quick_c[1]},{quick_c[2]},{quick_c[3]})["highway"="bus"];out;
    """

print(query)
result = api.query(query)
#result = api.query("node(50.745,7.17,50.75,7.18);out;")
with open("output.txt", "w") as f:
    for x in result.nodes:
        #print(x.__dict__)
        if 'name' in x.tags:
            f.write(f"{x.lat},{x.lon} {x.tags['name']}\n")
            #print(f"{x.lat},{x.lon} {x.tags['name']}")