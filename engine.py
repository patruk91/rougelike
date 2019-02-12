import os


import data_manager


filename = "levels/Level1.txt"
MOVE_ADD = 1
MOVE_SUB = -1
HERO_BEGIN_POSITION = [1, 20]


def get_char_in_terminal():
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return char


def movement():
    level_map = data_manager.get_maps_from_file(filename)
    hero_coordinates = HERO_BEGIN_POSITION
    level_map[hero_coordinates[1]][hero_coordinates[0]] = "@"
    print_some(level_map)
    get_char = ""
    while get_char != "q":
        get_char = get_char_in_terminal()
        os.system('clear')

        if get_char == "d":
            level_map = move_horizontally(get_char, level_map, MOVE_ADD, hero_coordinates)
            hero_coordinates = update_hero_coordinates(get_char, hero_coordinates, MOVE_ADD)

        elif get_char == "a":
            level_map = move_horizontally(get_char, level_map, MOVE_SUB, hero_coordinates)
            hero_coordinates = update_hero_coordinates(get_char, hero_coordinates, MOVE_SUB)

        elif get_char == "w":
            move_vertically(get_char, level_map, MOVE_SUB, hero_coordinates)
            hero_coordinates = update_hero_coordinates(get_char, hero_coordinates, MOVE_SUB)

        elif get_char == "s":
            move_vertically(get_char, level_map, MOVE_ADD, hero_coordinates)
            hero_coordinates = update_hero_coordinates(get_char, hero_coordinates, MOVE_ADD)


def move_horizontally(get_char, level_map, move, hero_position):
    erase_hero = erase_old_hero_position(level_map, hero_position)
    updated_pos = update_hero_coordinates(get_char, hero_position, move)
    updated_level_map = place_new_hero_position(erase_hero, updated_pos)

    print_some(updated_level_map)
    return updated_level_map


def move_vertically(get_char, level_map, move, hero_position):
    erase_hero = erase_old_hero_position(level_map, hero_position)
    updated_pos = update_hero_coordinates(get_char, hero_position, move)
    updated_level_map = place_new_hero_position(erase_hero, updated_pos)

    print_some(updated_level_map)
    return updated_level_map


def erase_old_hero_position(level_map, hero_position):
    x_position = hero_position[0]
    y_position = hero_position[1]
    level_map[y_position][x_position] = " "
    return level_map


def place_new_hero_position(level_map, hero_updated_position):
    x_position = hero_updated_position[0]
    y_position = hero_updated_position[1]
    level_map[y_position][x_position] = "@"
    return level_map


def update_hero_coordinates(get_char, hero_position, move):
    x_position = hero_position[0]
    y_position = hero_position[1]
    if get_char in ["d", "a"]:
        x_position += move
    elif get_char in ["w", "s"]:
        y_position += move
    return [x_position, y_position]


def print_some(level):
    for line in level:
        print(line)

# x = get_char_in_terminal()
# print(x)
print(movement())