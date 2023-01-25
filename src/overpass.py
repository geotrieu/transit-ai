import overpy
import inspect
api = overpy.Overpass()

quick_c = [43.75453102373179,-79.30420406128427,43.74657570660966,-79.28936830192336]
#quick_c is quick coordinate, paste in two coordinates and it will be re-ordered for OSM as the bounding box
if quick_c[2] < quick_c[0]:
    t = quick_c[0]
    quick_c[0] = quick_c[2]
    quick_c[2] = t
if quick_c[3] < quick_c[1]:
    t = quick_c[1]
    quick_c[1] = quick_c[3]
    quick_c[3] = t

print(quick_c)

result = api.query(f"""
    node({quick_c[0]},{quick_c[1]},{quick_c[2]},{quick_c[3]})["highway"="bus_stop"];
    out;
    """)
# result = api.query("node(50.745,7.17,50.75,7.18);out;")
print(result.nodes)
for x in result.nodes:
    #print(x.__dict__)
    print(f"{x.lat},{x.lon} {x.tags['name']}")