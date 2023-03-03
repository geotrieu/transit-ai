import overpy
import pandas as pd
import csv
api = overpy.Overpass()

class city_amenity_grabber:
    def grab_city_name_coords(self, middle_coordinate):

        coordinate_query = f"""
            is_in({middle_coordinate[0]}, {middle_coordinate[1]})->.a;
            rel(pivot.a)[boundary=administrative];
            out tags;
            """
        

        coordinate_result = api.query(coordinate_query)
        admin_levels = []

        # try place relation first, safest option
        for x in coordinate_result.relations:
            try:
                if x.tags["place"] == "city" or x.tags["place"] == "town":
                    return x.tags["name"]
            except:
                pass

        # if not found, find via admin levels. may vary and produce bad results
        for x in coordinate_result.relations:
            admin_levels.append(int(x.tags["admin_level"]))
        #pick lowest admin level that is over 9
        desired_level = [x for x in admin_levels if x <= 8]
        desired_level = max(desired_level)
        for x in coordinate_result.relations:
            if int(x.tags["admin_level"]) == desired_level:
                return x.tags["name"]
        """ for x in coordinate_result.relations:
            try:
                print(x.tags)
                if x.tags["place"] == "city" or x.tags["place"] == "town":
                    if x.tags["boundary"] == "administrative":
                        return x.tags["name"]
            except:
                pass """

    def write_amenity_from_coords(self, middle_coordinate, amenity, filepath):
        m = 50000 # metres
        city_name = self.grab_city_name_coords(middle_coordinate)
        print(city_name)
        query = f"""
            [out:json];
            area[name="{city_name}"];
            (node["amenity"="{amenity}"](area)(around:{m}, {middle_coordinate[0]}, {middle_coordinate[1]}););
            out;
            """
        

        result = api.query(query)
        print(result)
        #result = api.query("node(50.745,7.17,50.75,7.18);out;")
        lat, lon = [], []
        with open(filepath, "w", newline="", encoding='utf-8') as f:
            writer = csv.writer(f)
            for x in result.nodes:
                #print(x.__dict__)
                if 'name' in x.tags:
                    #f.write(f"{x.lat},{x.lon},{x.tags['name']}\n")
                    writer.writerow([x.lat,x.lon,x.tags['name']])
                    lat.append(x.lat)
                    lon.append(x.lon)
        return self.return_df(lat, lon)

    def return_df(self, lat, lon):
        d = {"lat": lat, "lon": lon}
        df = pd.DataFrame(data=d)
        return df

if __name__ == "__main__":
    p = city_amenity_grabber()
    c = [46.27736, -123.12833]
    # c is a coordinate in any city. c will return the name of the city, which will then pull all amenities inside of the city, in a dataframe.
    # this main function is a demonstration of how to import it and implement it
    df = p.write_amenity_from_coords(c,"community_centre","community_centre.csv")
    #print(df)

    # LIST OF AMENITIES
    # https://wiki.openstreetmap.org/wiki/Key:amenity
#%%
