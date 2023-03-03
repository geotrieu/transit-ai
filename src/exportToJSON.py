import json
import random
import pandas as pd
def getDarkColour():
    r = random.randint(0, 128)
    g = random.randint(0, 128)
    b = random.randint(0, 128)
    hex_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return hex_code

def exportToJSON(lines, stations, filename, customColors = []):
    obj = {
        "lines": []
    }
    for idx, line in enumerate(lines):
        stationsArr = []

        df = pd.DataFrame()
        df['lat'] = stations[idx][0]
        df['long'] = stations[idx][1]

        for pt in zip(line[0], line[1]):

            match = (df['lat'] == pt[0]) & (df['long'] == pt[1])

            if match.any():
                stat = True
            else:
                stat = False

            stationsArr.append({
                "lat": pt[0],
                "long": pt[1],
                "station": stat
            })
        lineObj = {
            "line_name": idx,
            "colour": customColors[idx] if len(customColors) > idx else getDarkColour(),
            "stations": stationsArr
        }
        obj["lines"].append(lineObj)

    with open('../res/output/' + filename + '.json', 'w') as fp:
        json.dump(obj, fp)