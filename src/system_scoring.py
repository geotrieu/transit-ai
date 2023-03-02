from numpy import linalg as la
import statistics
from misc_utility import *

MAX_SCORING_DISTANCE = 1 # Set max walking distance

# Scores a Transit System. Returns the system score and an array of all the line scores
def scoreSystem(gridPoints, stations):
    gp = list(zip(list(gridPoints["lat"]), list(gridPoints["long"]), list(gridPoints["score"]))) # Put all grid locations in a usable format
    lineScores = []
    for line in stations:
        stationScores = []
        for station in zip(line[0], line[1]):
            includedScores = []
            for point in gp:
                #if point[2] != 0 and la.norm([point[0] - station[0], point[1] - station[1]]) < MAX_SCORING_DISTANCE:
                if point[2] != 0 and getDistance((point[0], point[1]), station) < MAX_SCORING_DISTANCE:
                    includedScores.append(point[2])
            #print(statistics.mean(includedScores))
            stationScores.append(statistics.mean(includedScores))
        lineScores.append(statistics.mean(stationScores))

    return (statistics.mean(lineScores), lineScores)