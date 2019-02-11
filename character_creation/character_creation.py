import ui
import common


def create_character(points):
    points = 5
    statistics = {"HP": 75, "DEF": 0, "ATC": 1, "EXP": 0, "LVL": 1}
    ui.show_character_creation_screen(statistics, points)

    while points > 0:
        is_answer_correct = False
        while not is_answer_correct:
            stat_to_add = ui.get_string_input("Enter 'H', 'h', 'D', 'd' or 'A', 'a' to add statistic: ")
            is_answer_correct = common.validate_string_input(stat_to_add, ["H", "D", "A", "h", "d", "a"])
        if stat_to_add in ["h", "H"]:
            statistics["HP"] += 5
        elif stat_to_add in ["D", "d"]:
            statistics["DEF"] += 1
        elif stat_to_add in ["A", "a"]:
            statistics["ATC"] += 1
        ui.show_character_creation_screen(statistics, points)
        points -= 1

    return statistics
