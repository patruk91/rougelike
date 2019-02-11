import data_manager
import character_creation
import ui
import common


def menu():
    while True:
        answer = ui.menu_option()
        if common.validate_string_input(answer, condition=["1", "2", "3", "4"]):
            if answer == "1":
                pass
            elif answer == "2":
                pass
            elif answer == "3":
                pass
            elif answer == "4":
                exit()
   
menu()
