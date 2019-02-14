import data_manager
import ui
import common
import os
import engine
import character_creation.character_creation as char_cr


def menu():
    map_iterator = 0
    answer = ""
    os.system('clear')
    while answer != "4":
        print(data_manager.load_ascii_ar("ascii_ar/menu_art.txt"))
        answer = ui.menu_option()
        if common.validate_string_input(answer, condition=["1", "2", "3", "4"]):
            if answer == "1":
                char_stats = char_cr.create_character(5, {}, True)
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
