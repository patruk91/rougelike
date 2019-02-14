import data_manager
import ui
import common
import os
import engine
import character_creation.character_creation as char_cr


def menu():
    map_iterator = 0
    points_to_spend = 5
    char_creation = True
    answer = ""
    os.system('clear')
    while answer != "4":
        print(data_manager.load_ascii_art("ascii_art/menu_art.txt"))
        answer = ui.menu_option()
        if common.validate_string_input(answer, condition=["1", "2", "3", "4"]):
            if answer == "1":
                char_stats = char_cr.create_character(points_to_spend, {}, char_creation)
                inv = {}
                os.system('clear')

                # start engine module
                engine.engine_work(char_stats, inv, map_iterator)

            elif answer == "2":
                pass
            elif answer == "3":
                pass


def main():
    menu()


if __name__ == "__main__":
    main()
