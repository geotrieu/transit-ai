from radius_amenity_finder import city_amenity_grabber
import os
from os.path import dirname as up

p = city_amenity_grabber()
c = [43.65975219556051, -79.39142338042639]
# c is a coordinate in any city. c will return the name of the city, which will then pull all amenities inside of the city, in a dataframe.
# this main function is a demonstration of how to import it and implement it
amentities = [
    "community_centre",
    "food_court",
    "library",
    "restaurant",
    "school",
    "university"
]
for x in amentities:
    path = os.path.join(up(up(__file__)), "res", "datasets", "csv", "toronto", f"{x}.csv")
    print(path)
    df = p.write_amenity_from_coords(c, x, path)
#print(df)

# LIST OF AMENITIES
# https://wiki.openstreetmap.org/wiki/Key:amenity