import overpy
import pandas as pd


def get_input():
    print("\nEnter southern-most latitude:")
    latitude_s = str(43.582520)
    print("\nEnter western-most longitude:")
    longitude_w = str(-79.542173)
    print("\nEnter northern-most latitude:")
    latitude_n = str(43.960911)
    print("\nEnter eastern-most longitude:")
    longitude_e = str(-79.117140)

    print("\nEnter latitude:")
    latitude = str(43.726884)
    print("\nEnter longitude:")
    longitude = str(-79.480763)
    print("\nEnter radius in meter:")
    radius = str(10000)
    # test data: ['44.247676', '-76.558016', '44.285856', '-76.470983',
    # '44.246383', '-76.548668', '150000']
    return [latitude_s, longitude_w, latitude_n, longitude_e,
            latitude, longitude, radius]


# The values are, in order: southern-most latitude, western-most longitude, northern-most latitude, eastern-most
# longitude.
def get_hospital_query_bbox(user_input):
    query = """[out:json][timeout:180];(node["amenity"="hospital"](""" + user_input[0] + ',' + user_input[1] + ',' + \
            user_input[2] + ',' + user_input[3] + """););out body;>;out skel qt;"""
    return query


# circle and radius
def get_hospital_query_rad(user_input):
    query = """[out:json][timeout:180];(node["amenity"="college"](around:""" + user_input[6] + ',' + user_input[
        4] + ',' + \
            user_input[5] + """););out body;>;out skel qt;"""
    return query


def extract_nodes_data_from_OSM(built_query, filename):
    api = overpy.Overpass()
    result = api.query(built_query)
    list_of_node_tags = []
    for node in result.nodes:  # from each node , get the all tags information
        node.tags['latitude'] = node.lat
        node.tags['longitude'] = node.lon
        node.tags['id'] = node.id
        list_of_node_tags.append(node.tags)
    data_frame = pd.DataFrame(list_of_node_tags)
    data_frame.to_csv(filename + ".csv")
    return data_frame


if __name__ == '__main__':
    user_input = get_input()
    query = get_hospital_query_bbox(user_input)
    data_frame = extract_nodes_data_from_OSM(query, 'hospital_bbox')
    query_around = get_hospital_query_rad(user_input)
    data_frame = extract_nodes_data_from_OSM(query_around, 'hospital_rad')
