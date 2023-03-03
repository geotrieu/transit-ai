import json

d = {}
d["lines"] = []
d["lines"].append({
    "colour": "#00923f",
    "stations": [
        {
            "lat": 44.230149950539236,
            "long":  -76.48536201001498,
            "station": True
        },
        {
            "lat": 44.231780707158485,
            "long": -76.49566234477982,
            "station": False
        },
        {
            "lat": 44.23088813847274,
            "long":  -76.51450381468338,
            "station": True
        },
        {
            "lat": 44.23015275968255,
            "long": -76.52620966619993,
            "station": True
        }
    ]
})
d["lines"].append({
    "colour": "#ffff00",
    "stations": [
        {
            "lat": 44.231148408530046,
            "long":  -76.47955611478864,
            "station": True
        },
        {
            "lat": 44.23299222536197,
            "long": -76.49166663286621,
            "station": True
        },
        {
            "lat": 44.241089730861376,
            "long": -76.51159560725303,
            "station": True
        }

    ]
})
print(d)

with open("../components/data/kingston.json", "w") as f:
    json.dump(d, f, indent=4)