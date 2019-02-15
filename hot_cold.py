import os
import random
import data_manager
import ui
import common
import character_creation.character_creation as char_cr


def get_random_int(range_start, range_end):
    number = random.randint(range_start, range_end)

    return number


def check_guess(char_stats, number, numbers_end_range, damage, file_name):
    # guess = int(input("Enter an integer from 1 to {}: ".format(numbers_end_range)))
    guess = 999
    os.system('clear')
    print(data_manager.load_ascii_art(file_name))
    while number != guess and char_stats["HP"] > 0:
        ui.print_character_statistics(char_stats)
        guess = input("Guess an integer from 1 to {}: ".format(numbers_end_range))
        if common.check_is_number(guess, numbers_end_range):
            guess = int(guess)
            os.system('clear')
            if guess < number:
                print(data_manager.load_ascii_art(file_name))
                print("{} is to low".format(guess))
                if (damage - char_stats["DEF"]) >= 0:
                    char_stats["HP"] -= (damage - char_stats["DEF"])
            elif guess > number:
                print(data_manager.load_ascii_art(file_name))
                print("{} is to high".format(guess))
                if (damage - char_stats["DEF"]) >= 0:
                    char_stats["HP"] -= (damage - char_stats["DEF"])
        else:
            os.system('clear')
            print(data_manager.load_ascii_art(file_name))
    os.system('clear')
    if char_stats["HP"] > 0:
        char_stats["EXP"] += 4
        if char_stats["EXP"] >= 10:
            char_stats["EXP"] -= 10
            char_stats["LVL"] += 1
            char_stats = char_cr.create_character(2, char_stats)
            os.system('clear')

    return char_stats


def fight(char_stats, damage, file_name):
    end_range = 99 - char_stats["ATC"] * 2
    random_int = get_random_int(1, end_range)
    char_stats = check_guess(char_stats, random_int, end_range, damage, file_name)

    return char_stats
