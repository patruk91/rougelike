def get_maps_from_file(file_name):
    level_map = []
    with open(file_name, "r") as file_object:
        for line in file_object:
            level_map.append(line.rstrip().split("\n"))
    return level_map
