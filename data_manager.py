def get_maps_from_file(file_name):
    level_map = []
    with open(file_name, "r") as file_object:
        for line in file_object:
            line = list(line.rstrip())
            level_map.append(line)
    return level_map


def load_asci_art(file_name):
    with open(file_name, "r") as file_object:
        for art in file_object:
            art = file_object.read()
    return art
