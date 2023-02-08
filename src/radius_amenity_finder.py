import overpy
import pandas as pd
api = overpy.Overpass()

class city_amenity_grabber:
    def grab_city_name_coords(self, middle_coordinate):


        coordinate_query = f"""
            is_in({middle_coordinate[0]}, {middle_coordinate[1]})->.a;
            rel(pivot.a)[boundary=administrative];
            out tags;
            """

        coordinate_result = api.query(coordinate_query)
        for x in coordinate_result.relations:
            try:
                if x.tags["place"] == "city" or x.tags["place"] == "town":
                    if x.tags["boundary"] == "administrative":
                        return x.tags["name"]
            except:
                pass

    def write_amenity_from_coords(self, middle_coordinate, amenity):
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
        #result = api.query("node(50.745,7.17,50.75,7.18);out;")
        lat, lon = [], []
        with open("output.txt", "w", encoding='utf-8') as f:
            for x in result.nodes:
                #print(x.__dict__)
                if 'name' in x.tags:
                    f.write(f"{x.lat},{x.lon} {x.tags['name']}\n")
                    lat.append(x.lat)
                    lon.append(x.lon)
        return self.return_df(lat, lon)

    def return_df(self, lat, lon):
        d = {"lat": lat, "lon": lon}
        df = pd.DataFrame(data=d)
        return df

if __name__ == "__main__":
    p = city_amenity_grabber()
    c = [43.360976206013945, -79.78070061430267]
    df = p.write_amenity_from_coords(c,"restaurant")
    print(df)

    # LIST OF AMENITIES
    # https://wiki.openstreetmap.org/wiki/Key:amenity