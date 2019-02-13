import os
import random
import data_manager
import ui
import common
import character_creation


def get_random_int(range_start, range_end):
    number = random.randint(range_start, range_end)

    return number


def check_guess(char_stats, number, numbers_end_range, damage):
    # guess = int(input("Enter an integer from 1 to {}: ".format(numbers_end_range)))
    guess = 999
    os.system('clear')
    while number != guess and char_stats["HP"] > 0:
        print("FIGHT")
        ui.print_character_statistics(char_stats)
        guess = input("Enter an integer from 1 to {}: ".format(numbers_end_range))
        if common.check_is_number(guess, numbers_end_range):
            guess = int(guess)
            os.system('clear')
            if guess < number:
                print("guess is low")
                char_stats["HP"] -= damage
            elif guess > number:
                print("guess is high")
                char_stats["HP"] -= (damage - char_stats["DEF"])
    if char_stats["HP"] > 0:
        print("You defeted enemy!")
        char_stats["EXP"] += 2
        if char_stats["EXP"] == 10:
            char_stats["EXP"] = 0
            char_stats["LVL"] += 1
            char_stats = char_stats.create_character(2)

    return char_stats


def fight(char_stats, damage):
    end_range = 99 - char_stats["ATC"] * 4
    random_int = get_random_int(1, end_range)
    char_stats = check_guess(char_stats, random_int, end_range, damage)

    return char_stats
