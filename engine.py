import os


import data_manager
import ui
import hot_cold
import common
import items.items
import inventory.inventory
# import character_creation.character_creation as char_cr



MOVE = {"FORWARD": 1, "BACKWARD": -1}
IMPASSABLE_ELEMENTS = ["#", "B", "R"]
INTERACTION_ELEMENTS = ["W", "F", "C", "&", "D"]
HERO_BEGIN_POSITION = [[1, 20], [1, 13], [1, 19], [1, 17]]
HERO_END_POSITION = [[2, 20], [2, 13], [2, 19], [2, 17]]
LEVELS_NAME = ['levels/level1.txt', 'levels/level2.txt', 'levels/level3.txt', 'levels/level4.txt']


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


def handle_movement(filename, char_stats, MAP_ITERATOR, inv):
    """
    Main function to handle hero movement. Hero can move by pressing
    keys: "w", "a", "s", "d".
    :param filename: text file: where stored level
    :param char_stats: dict: basic hero statistic
    """
    level_map = data_manager.get_maps_from_file(filename)
    old_hero_coordinates = HERO_BEGIN_POSITION[0]
    level_map[old_hero_coordinates[1]][old_hero_coordinates[0]] = "@"
    # place hero on map by coordinates

    ui.display_level_map(level_map, char_stats, inv)
    get_char = ""

    while get_char != "q":
        get_char = get_char_in_terminal()
        os.system('clear')
        new_hero_coordinates = update_hero_coordinates(get_char, old_hero_coordinates, MOVE)
        if check_if_impassable(new_hero_coordinates, level_map):
            if check_if_item_interaction(new_hero_coordinates, level_map):
                character = get_character_at_position(level_map, new_hero_coordinates)

                damage = 10
                if character == "W":
                    loot = items.items.weapons()
                    char_stats["ATC"] += loot[1]
                    inventory.inventory.add_to_inventory(inv, loot)
                    del inv[loot[1]]     
                elif character == "F":
                    loot = items.items.food()
                    if char_stats["HP"] < 100:
                        char_stats["HP"] += loot[1]
                    if char_stats["HP"] > 100:
                        char_stats["HP"] = 100
                elif character == "C":
                    loot = items.items.clotches()
                    char_stats["DEF"] += loot[1]
                elif character == "&":
                    char_stats = hot_cold.fight(char_stats, damage)
                    if char_stats["HP"] <= 0:
                        end_screen = data_manager.load_asci_art("asci_art/game_over.txt")
                        print(end_screen)
                elif character == "D":
                    MAP_ITERATOR += 1
                    level_map = common.handle_transfer_to_next_map(LEVELS_NAME[MAP_ITERATOR])


                    new_hero_coordinates = HERO_BEGIN_POSITION[MAP_ITERATOR]
                    old_hero_coordinates = HERO_END_POSITION[MAP_ITERATOR]
                    get_char = "a"


                # trigger_interaction(char_stats, character)
            updated_level_map = update_map(get_char, level_map, old_hero_coordinates, new_hero_coordinates)
            old_hero_coordinates = update_hero_coordinates(get_char, old_hero_coordinates, MOVE)
            ui.display_level_map(updated_level_map, char_stats, inv)
        else:
            ui.display_level_map(level_map, char_stats, inv)


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
    x_position = new_hero_coordinates[0]
    y_position = new_hero_coordinates[1]
    if level_map[y_position][x_position] in IMPASSABLE_ELEMENTS:
        return False
    return True


def check_if_item_interaction(new_hero_coordinates, level_map):
    """
    Check if hero encountered elements with interactions: ("W", "F", "C", "&", "D")
    :param new_hero_coordinates: list: hero coordinates on map, where he want to move
    :param level_map: list of lists: designed map from text file
    :return: boolean: True if he encountered elements
    """
    x_position = new_hero_coordinates[0]
    y_position = new_hero_coordinates[1]
    if level_map[y_position][x_position] in INTERACTION_ELEMENTS:
        return True
    return False

#
# def trigger_interaction(char_stats, character):
#     """
#     Trigger other functions due to a reaction with a given element on level map
#     :param new_hero_coordinates: list: hero coordinates on map
#     :param level_map: designed map from text file
#     :param char_stats: dict: basic hero statistic
#     :return:
#     """
#     damage = 5
#
#     if character == "W":
#         pass
#     elif character == "F":
#         pass
#     elif character == "C":
#         pass
#     elif character == "&":
#         char_stats = hot_cold.fight(char_stats, damage)
#         if char_stats["HP"] <= 0:
#             end_screen = data_manager.load_asci_art("asci_art/game_over.txt")
#             print(end_screen)
#     elif character == "D":
#         pass


def get_character_at_position(level_map, new_hero_coordinates):
    x_position = new_hero_coordinates[0]
    y_position = new_hero_coordinates[1]
    character = level_map[y_position][x_position]
    return character

# x = get_char_in_terminal()
# print(x)
# print(handle_movement(filename='levels/level1.txt', char_stats=char_cr.create_character(5)))
