import os


def show_character_creation_screen(char_stats, free_points):
    os.system('clear')
    print("CHARACTER CREATION\n")
    print("Your statistics:\n{:^5} - HP\n{:^5} - DEF\n{:^5} - ATC".format(char_stats["HP"], char_stats["DEF"], char_stats["ATC"]))
    print("Points to spend for stats: {}".format(free_points))
    print("Press H to add 6 points to HP")
    print("Press D to add 1 point to DEF")
    print("Press A to add 1 pint to ATC")


def get_string_input(question):
    answer = input(question)

    return answer


def print_error(message):
    print("ERROR: " + message)


def menu_option():
    print("""Rougelike Menu
(1)Play Game
(2)Highscore
(3)Sth
(4)Exit Game""")
    answer = input("Choose number: ")
    return answer


def print_character_statistics(char_stats):
    string = "HP:{:>5}\tDEF:{:>5}\tATC:{:>5}\tEXP:{:>5}\tLVL:{:>5}"
    print(string.format(*char_stats.values()))


def display_map_instructions():
    print("Press W A S D to move | #-wall, B-bush, R-river, @-hero, &-enemy, F-food, D-next level, W-weapon, C-clothes")


def display_inventory(inventory):
    list_of_items = []
    for keys in inventory.keys():
        list_of_items.append(keys)
    print("Inventory:")
    string = "{},\t" * len(list_of_items)
    print(string.format(*list_of_items))

        


def display_level_map(level_map, char_stats, inv):
    """
    Display map to user
    :param level_map: list of lists: map from text file or updated when program is running
    """
    # need to be change to "".join..? Patryk
    print_character_statistics(char_stats)
    for line in level_map:
        print("".join(line))
    display_map_instructions()
    display_inventory(inv)
