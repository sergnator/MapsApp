from MapsAPI import create_map_image

map_params = {
    "ll": ",".join(['0', '0']),
    "spn": ",".join(['40', '40']),
    "l": "map"
}

create_map_image(map_params).show()