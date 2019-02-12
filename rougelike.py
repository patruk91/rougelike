import data_manager
import ui
import common
import character_creation.character_creation as char_cr
import os
import engine


def menu():
    os.system('clear')
    while True:
        data_manager.load_asci_art("asci_art/menu_art.txt")
        answer = ui.menu_option()
        if common.validate_string_input(answer, condition=["1", "2", "3", "4"]):
            if answer == "1":
                char_stats = char_cr.create_character(5)
                os.system('clear')
                data_manager.get_maps_from_file('levels/level1.txt')
                ui.print_character_statistics(char_stats)
                engine.handle_movement()
            elif answer == "2":
                pass
            elif answer == "3":
                pass
            elif answer == "4":
                exit()


def main():
    menu()

if __name__ == "__main__":
    main()
