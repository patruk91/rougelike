import random


def get_random_int(range_start, range_end):
    number = random.randint(range_start, range_end)

    return number


def check_guess(char_stats, numbers, numbers_end_range, damage):
    guess = int(input("Enter an integer from 1 to {}: ".format(numbers_end_range)))
    while number != guess or char_stats["HP"] > 0:
        if guess < number:
            print("guess is low")
            char_stats["HP"] -= damage

        elif guess > number:
            print("guess is high")
            char_stats["HP"] -= damage
        guess = int(input("Enter an integer from 1 to {}: ".format(numbers_end_range)))
    print("you guessed it!")

    return char_stats


def fight(char_stats, damage):
    random_int = get_random_int(1, 99)
    check_guess(char_stats, random_int, 99, damage)
