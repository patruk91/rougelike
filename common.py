import ui
import data_manager
import time


def validate_string_input(string, condition=""):
    """
    Validate if string from input is not empty and is in given condition.
    Condition must be in format: ["a", "b", "c".....]

    >>> validate_string_input("", ["s"])
    ERROR: Input can't be empty
    False
    >>> validate_string_input("s", ["c"])
    ERROR: Input must be in ['c']
    False
    >>> validate_string_input("Not_empty", "")
    True
    >>> validate_string_input("content", ["content"])
    True
    """
    is_string_correct = True
    if not string:
        ui.print_error("Input can't be empty")
        is_string_correct = False
    if condition:
        if string:
            if string not in condition:
                ui.print_error("Input must be in {}".format(condition))
                is_string_correct = False

    return is_string_correct


def check_is_number(user_data, end_range):
    """
    Check if user provided a number for duration and start time
    :param user_data: parameter provided by user
    :return: boolean
    """
    if user_data.isdigit() and end_range >= int(user_data) >= 1:
        return True
    return False


def handle_transfer_to_next_map(map_number):
    level_map = data_manager.get_maps_from_file(map_number)
    return level_map


def check_if_item_interaction(new_hero_coordinates, level_map):
    """
    Check if hero encountered elements with interactions: ("W", "F", "C", "&", "D")
    :param new_hero_coordinates: list: hero coordinates on map, where he want to move
    :param level_map: list of lists: designed map from text file
    :return: boolean: True if he encountered elements
    """
    result = False
    INTERACTION_ELEMENTS = ["W", "F", "C", "&", "D"]
    x_position = new_hero_coordinates[0]
    y_position = new_hero_coordinates[1]
    if level_map[y_position][x_position] in INTERACTION_ELEMENTS:
        result = True
    return result


def get_character_at_position(level_map, new_hero_coordinates):
    x_position = new_hero_coordinates[0]
    y_position = new_hero_coordinates[1]
    character = level_map[y_position][x_position]
    return character


def game_time(start_time):
    end_time = time.time()
    time_ = round(end_time - start_time, 2)

    return time_


def get_user_score(char_stats, play_time):
    exp = char_stats["EXP"]
    if char_stats["EXP"] == 0:
        exp = 1
    final_score = str(int(char_stats["EXP"] * 3.14 * int(play_time)))

    return final_score
