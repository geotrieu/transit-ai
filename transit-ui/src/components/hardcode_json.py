import json

d = {}
d["lines"] = []
d["lines"].append({
    "line_name": "line1",
    "colour": "green",
    "stations": [
        {
            "lat": 12,
            "long": -45,
            "station": True
        },
        {
            "lat": 12,
            "long": -46,
            "station": False
        }
    ]
})
d["lines"].append({
    "line_name": "line2",
    "colour": "red",
    "stations": [
        {
            "lat": 34,
            "long": -40,
            "station": False
        },
        {
            "lat": 35,
            "long": -46,
            "station": False
        }
    ]
})
print(d)

with open("dict.json", "w") as f:
    json.dump(d, f, indent=4)