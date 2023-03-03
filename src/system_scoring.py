from numpy import linalg as la
import statistics
from misc_utility import *
import math
import pandas as pd

MAX_SCORING_DISTANCE = 1  # Set max walking distance
RADIUS = 6371  #in km

def distance(point1, point2):
    lat1, long1 = point1
    lat2, long2 = point2

    x1 = RADIUS * math.cos(math.radians(lat1)) * math.cos(math.radians(long1))
    y1 = RADIUS * math.cos(math.radians(lat1)) * math.sin(math.radians(long1))
    x2 = RADIUS * math.cos(math.radians(lat2)) * math.cos(math.radians(long2))
    y2 = RADIUS * math.cos(math.radians(lat2)) * math.sin(math.radians(long2))

    return la.norm([x2 - x1, y2 - y1])


# Scores a Transit System. Returns the system score and an array of all the line scores
def scoreSystem(gridPoints, stations):
    gp = list(zip(list(gridPoints["lat"]), list(gridPoints["long"]),
                  list(gridPoints["score"])))  # Put all grid locations in a usable format
    lineScores = []
    for line in stations:
        stationScores = []
        for station in zip(line[0], line[1]):
            includedScores = []
            for point in gp:
                if point[2] != 0 and distance((point[0], point[1]), station) < MAX_SCORING_DISTANCE:
                    includedScores.append(point[2])
            stationScores.append(statistics.mean(includedScores) if (len(includedScores) != 0) else 0)
        lineScores.append(statistics.mean(stationScores))

    return (statistics.mean(lineScores), lineScores)
