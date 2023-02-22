def getBounds(latitudes, longitudes, precision):
    topLat = round(latitudes.max(), precision)
    bottomLat = round(latitudes.min(), precision)
    leftLong = round(longitudes.min(), precision)
    rightLong = round(longitudes.max(), precision)
    return (topLat, bottomLat, leftLong, rightLong)