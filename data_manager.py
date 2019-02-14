def get_maps_from_file(file_name):
    level_map = []
    with open(file_name, "r") as file_object:
        for line in file_object:
            line = list(line.rstrip())
            level_map.append(line)
    return level_map


def load_ascii_art(file_name):
    with open(file_name, "r") as file_object:
        for art in file_object:
            art = file_object.read()
    return art


def save_final_score(file_name, user_score):
    with open(file_name, "a+") as my_file:
        user_score = ';'.join(user_score)
        my_file.write(user_score + "\n")


def get_user_score(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    content = [element.rstrip().split(";") for element in lines]

    return content
