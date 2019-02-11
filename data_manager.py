def get_maps_from_file(file_name):

    with open(file_name, "r") as file:
        lines = file.read()
    return lines
