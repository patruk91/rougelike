import data_manager
import character_creation


def menu():
    print("Rougelike Menu")
    print("1. Start Game")
    print("2. Highscore")
    print("3. Exit Game")
    ask_user_for_data = int(input("Choose what do u want to do!: "))
    if ask_user_for_data == 1:
        char_stats = character_creation.create_character()
    elif ask_user_for_data == 2:
        pass
        #odpalamy highscore
    else:
        exit()
    
menu()
