import data_manager
<<<<<<< HEAD
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
   
=======
import character_creation.character_creation as char_cr
import ui
import os


def menu():
    print("Rougelike Menu")
    print("1. Start Game")
    print("2. Highscore")
    print("3. Exit Game")
    ask_user_for_data = int(input("Choose what do u want to do!: "))
    if ask_user_for_data == 1:
        char_stats = char_cr.create_character(5)
        os.system('clear')
        ui.print_character_statistics(char_stats)
    elif ask_user_for_data == 2:
        pass
        #odpalamy highscore
    else:
        exit()
    
>>>>>>> 4b9155a7a35130bd4fe233650e96afd9dbe1f5a4
menu()
