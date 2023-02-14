import time
import googlemaps
import pandas as pd
from googlemaps.geocoding import geocode
import ast


def user_input(map_client):
    # User fill in address, transfer to lat, lon automatically
    address = '77 Wynford Dr, North York, ON'
    (lat, lon) = map(map_client.geocode(address=address)[0]['geometry']['location'].get, ('lat', 'lng'))
    # amenity input
    amenity = 'university'
    # radius in metres
    radius = 10000

    return lat, lon, amenity, radius


def search(lat, lon, search_string, distance, map_client):
    amenity_list = []

    response = map_client.places_nearby(
        location=(lat, lon),
        keyword=search_string,
        radius=distance
    )
    amenity_list.extend(response.get('results'))
    next_page_token = response.get('next_page_token')

    while next_page_token:
        time.sleep(2)
        response = map_client.places_nearby(
            location=(lat, lon),
            keyword=search_string,
            radius=distance,
            page_token=next_page_token
        )
        amenity_list.extend(response.get('results'))
        next_page_token = response.get('next_page_token')

    df = pd.DataFrame(amenity_list)
    df['url'] = 'https://www.google.com/maps/place/?q=place_id:' + df['place_id']
    df = df.drop(
        columns=["business_status", "icon", "icon_background_color", "icon_mask_base_uri", "icon_mask_base_uri",
                 "photos", "place_id", "rating", "reference", "scope", "plus_code", "opening_hours", "url"])

    df.to_excel('{0}.xlsx'.format(search_string), index=False)

    # change original format to usable format
    df = pd.read_excel('{0}.xlsx'.format(search_string))
    df_list = df.values.tolist()
    lat_list = []
    lon_list = []
    for i in df_list:
        res = ast.literal_eval(i[0])
        lat_list.append(res['location']['lat'])
        lon_list.append(res['location']['lng'])
    df["lat"] = lat_list
    df["lng"] = lon_list
    df = df.drop(
        columns=["geometry", "types"])

    print(df)
    df.to_excel('{0}.xlsx'.format(search_string), index=False)


if __name__ == "__main__":
    API_KEY = 'AIzaSyDfuS8XpS-iWkalk9VJ4Wa6ExFuAXATKu8'
    map_client = googlemaps.Client(API_KEY)

    lat, lon, amenity, radius = user_input(map_client)
    search(lat, lon, amenity, radius, map_client)
