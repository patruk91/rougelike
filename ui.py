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
