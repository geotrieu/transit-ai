import json

d = {}
d["lines"] = []
d["lines"].append({
    "colour": "#34dd3d",
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
    "colour": "#80923f",
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
d["lines"].append({
    "colour": "#00923f",
    "stations": [
        {
            "lat": 43.66232131647472,
            "long": -79.42576367913883,
            "station": True
        },
        {
            "lat": 43.678162843940655,
            "long": -79.34930882676771,
            "station": False
        },
        {
            "lat": 43.69138551428441,
            "long": -79.28731323953545,
            "station": True
        }
    ]
})
print(d)

with open("../components/data/dict.json", "w") as f:
    json.dump(d, f, indent=4)