import os


import data_manager
import ui


filename = "levels/Level1.txt"
MOVE_ADD = 1
MOVE_SUB = -1
HERO_BEGIN_POSITION = [1, 20]
MOVE = [MOVE_ADD, MOVE_SUB]


def get_char_in_terminal():
    """
    Get character from user in terminal, when he push the button.
    :return: char: keyboard character
    """
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


def handle_movement():
    """
    Main function to handle hero movement. Hero can move by pressing
    keys: "w", "a", "s", "d".
    """
    level_map = data_manager.get_maps_from_file(filename)
    hero_coordinates = HERO_BEGIN_POSITION
    level_map[hero_coordinates[1]][hero_coordinates[0]] = "@"
    ui.display_level_map(level_map)
    get_char = ""
    while get_char != "q":
        get_char = get_char_in_terminal()
        os.system('clear')

        if get_char == "d":
            level_map = move_horizontally(get_char, level_map, MOVE, hero_coordinates)
        elif get_char == "a":
            level_map = move_horizontally(get_char, level_map, MOVE, hero_coordinates)
        elif get_char == "w":
            move_vertically(get_char, level_map, MOVE, hero_coordinates)
        elif get_char == "s":
            move_vertically(get_char, level_map, MOVE, hero_coordinates)

        hero_coordinates = update_hero_coordinates(get_char, hero_coordinates, MOVE)


def move_horizontally(get_char, level_map, move, hero_position):
    """
    Update hero position in horizontal directions.
    :param get_char: char: key pressed by user (necessary here: "a", "d")
    :param level_map: list of lists: map from text file
    :param move: list: constant, hero can move forward or backward (depend on character)
    :param hero_position: list: actual hero position on map
    :return: list of lists: updated map level with hero position
    """
    erase_hero = erase_old_hero_position(level_map, hero_position)
    updated_pos = update_hero_coordinates(get_char, hero_position, move)
    updated_level_map = place_new_hero_position(erase_hero, updated_pos)

    ui.display_level_map(updated_level_map)
    return updated_level_map


def move_vertically(get_char, level_map, move, hero_position):
    """
    Update hero position in vertical directions.
    :param get_char: char: key pressed by user (necessary here: "w", "s")
    :param level_map: list of lists: map from text file
    :param move: list: constant, hero can move forward or backward (depend on character)
    :param hero_position: list: actual hero position on map
    :return: list of lists: updated map level with hero position
    """
    erase_hero = erase_old_hero_position(level_map, hero_position)
    updated_pos = update_hero_coordinates(get_char, hero_position, move)
    updated_level_map = place_new_hero_position(erase_hero, updated_pos)

    ui.display_level_map(updated_level_map)
    return updated_level_map


def erase_old_hero_position(level_map, hero_position):
    """
    Erase hero position from map
    :param level_map: list of lists: map from text file
    :param hero_position: list: actual hero position on map to erase from level_map
    :return: list of lists: updated level_map without hero position
    """
    x_position = hero_position[0]
    y_position = hero_position[1]
    level_map[y_position][x_position] = " "
    return level_map


def place_new_hero_position(level_map, hero_updated_position):
    """
    Place on map new hero position
    :param level_map: list of lists: map from text file
    :param hero_updated_position: list: actual hero position on map to place on level_map
    :return: list of lists: updated level_map with new hero position
    """
    x_position = hero_updated_position[0]
    y_position = hero_updated_position[1]
    level_map[y_position][x_position] = "@"
    return level_map


def update_hero_coordinates(get_char, hero_position, move):
    """
    Update hero coordinates
    :param get_char: char: key pressed by user (necessary here: "w", "s")
    :param hero_position: list: hero position to update, depend on get_char
    :param move: list: constant, hero can move forward or backward (depend on character)
    :return: list: updated hero coordinates
    """
    x_position = hero_position[0]
    y_position = hero_position[1]
    move_add = move[0]
    move_sub = move[1]

    if get_char == "d":
        x_position += move_add
    elif get_char == "a":
        x_position += move_sub
    elif get_char == "w":
        y_position += move_sub
    elif get_char == "s":
        y_position += move_add
    return [x_position, y_position]



# x = get_char_in_terminal()
# print(x)
print(handle_movement())