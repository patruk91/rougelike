import data_manager
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
    
menu()
