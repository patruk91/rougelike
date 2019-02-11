import common


def show_character_creation_screen(char_stats, free_points):
    print("CHARACTER CREATION\n")
    print("Your statistics:\n{:^5} - HP\n{:^5} - DEF\n{:^5} - ATC".format(char_stats[HP], char_stats[DRF], char_stats[ATC]))
    print("Points to spend for stats: {}".format(free_points))
    print("Press H to add 6 points to HP")
    print("Press D to add 1 point to DEF")
    print("Press A to add 1 pint to ATC")
    while free_points > 0:
        is_answer_correct = False
        while not is_answer_correct:
            stat_to_add = get_string_input("Enter 'H', 'D' or A to add statistic: ")
            is_answer_correct = validate_string_input(stat_to_add)


def get_string_input("Enter 'H', 'D' or A to add statistic: "):
    input = input(question)

    return input

def print_error(message):
    print("ERROR: " + message)