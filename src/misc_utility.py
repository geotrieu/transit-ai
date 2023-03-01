from geopy.distance import geodesic

def getDistance(origin, stationCor):
    return abs(geodesic(origin, stationCor).meters/1000)