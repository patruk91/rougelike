import os
import data_manager


MOVE = {"FORWARD": 1, "BACKWARD": -1}


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


def handle_coordinates(get_char, hero_coordinates, filename):
    """
    Main function to handle hero movement. Hero can move by pressing
    keys: "w", "a", "s", "d".
    :param filename: text file: where stored level
    :param char_stats: dict: basic hero statistic
    """
    result = hero_coordinates
    level_map = data_manager.get_maps_from_file(filename)
    new_hero_coordinates = update_hero_coordinates(get_char, hero_coordinates, MOVE)
    if check_if_impassable(new_hero_coordinates, level_map):
        result = new_hero_coordinates
    return result


def update_map(get_char, level_map, old_hero_coordinates, new_hero_coordinates):
    """
    Update map level or return old one, depend on user key pressed
    :param get_char: char: key pressed by user
    :param level_map: list of lists: designed map from text file
    :param old_hero_coordinates: list: old(previous) hero coordinates on map
    :param new_hero_coordinates: list: actual hero coordinates on map
    :return: list of lists: updated level_map with placed hero at new coordinates
             or old level_map with placed hero at old coordinates
    """
    if get_char in ["w", "a", "s", "d"]:
        updated_level_map = hero_move(level_map, old_hero_coordinates, new_hero_coordinates)
        return updated_level_map
    return level_map


def hero_move(level_map, old_hero_coordinates, new_hero_coordinates):
    """
    Move hero on map in horizontal directions
    :param level_map: list of lists: designed map from text file
    :param old_hero_coordinates: list: old(previous) hero coordinates on map
    :param new_hero_coordinates: list: actual hero coordinates on map
    :return: list of lists: updated level_map with placed hero at new coordinates
    """
    erase_hero = erase_old_hero_position(level_map, old_hero_coordinates)
    updated_level_map = place_new_hero_position(erase_hero, new_hero_coordinates)
    return updated_level_map


def erase_old_hero_position(level_map, old_hero_coordinates):
    """
    Erase form map: old hero position
    :param level_map: list of lists: designed map from text file
    :param old_hero_coordinates: list: old(previous) hero coordinates on map
    :return: list of lists: updated level_map without old hero coordinates
    """
    x_position = old_hero_coordinates[0]
    y_position = old_hero_coordinates[1]
    level_map[y_position][x_position] = " "
    return level_map


def place_new_hero_position(level_map, hero_updated_position):
    """
    Place on map: new hero position
    :param level_map: list of lists: designed map from text file
    :param hero_updated_position: list: actual hero coordinates on map
    :return: list of lists: updated level_map with new hero coordinates
    """
    x_position = hero_updated_position[0]
    y_position = hero_updated_position[1]
    level_map[y_position][x_position] = "@"
    return level_map


def update_hero_coordinates(get_char, old_hero_coordinates, move):
    """
    Update hero coordinates/position
    :param get_char: char: key pressed by user
    :param old_hero_coordinates: list: hero position to update, depend on get_char
    :param move: dict: constant, hero can move forward or backward (depend on key pressed)
    :return: list: updated hero coordinates
    """
    x_position = old_hero_coordinates[0]
    y_position = old_hero_coordinates[1]
    move_forward = move.get("FORWARD", 0)
    move_backward = move.get("BACKWARD", 0)

    if get_char == "d":
        x_position += move_forward
    elif get_char == "a":
        x_position += move_backward
    elif get_char == "w":
        y_position += move_backward
    elif get_char == "s":
        y_position += move_forward
    return [x_position, y_position]


def check_if_impassable(new_hero_coordinates, level_map):
    """
    Check if hero encountered impassable elements: ("#", "B", "R")
    :param new_hero_coordinates: list: hero coordinates on map, where he want to move
    :param level_map: list of lists: designed map from text file
    :return: boolean: False if he encountered elements
    """
    result = True
    IMPASSABLE_ELEMENTS = ["#", "B", "R"]
    x_position = new_hero_coordinates[0]
    y_position = new_hero_coordinates[1]
    if level_map[y_position][x_position] in IMPASSABLE_ELEMENTS:
        result = False

    return result
