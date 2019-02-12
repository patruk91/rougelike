import data_manager
import ui
import common
import character_creation.character_creation as char_cr
import os


def menu():
    data_manager.load_asci_art("asci_art/menu_art.txt")
    while True:
        answer = ui.menu_option()
        if common.validate_string_input(answer, condition=["1", "2", "3", "4"]):
            if answer == "1":
                char_stats = char_cr.create_character(5)
                os.system('clear')
                ui.print_character_statistics(char_stats)
            elif answer == "2":
                pass
            elif answer == "3":
                pass
            elif answer == "4":
                exit()

menu()