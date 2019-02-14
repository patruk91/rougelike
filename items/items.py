import random


def weapons():
    """
    List of weapon available in game. Tuple schemat:(Item name, How many atack add)
    Return: Random weapon from list.
    """
    weapons_list = [("dagger", 3), ("axe", 5), ("pick", 4), ("stick", 1),
                    ("infinity edge", 10), ("bloodrazor", 8)]
    return weapons_list[random.randint(0, len(weapons_list)-1)]


def food():
    """
    List of food available in game. Tuple schemat:(Food name, How many HP add)
    Return: Random food from list.
    """
    food_list = [("ham", 10), ("meat", 6), ("melon", 6), ("apple", 5),
                 ("cake", 5), ("sweets", 4)]
    return food_list[random.randint(0, len(food_list)-1)]


def clotches():
    """
    List of clotches available in game. Tuple schemat:(Item name, How many DEFF add)
    Return: Random clotches from list.
    """
    clothes_list = [("brass helmet", 1), ("rainbow shield", 4),
                    ("doran shield", 1), ("plate armor", 2),
                    ("steel boots", 1), ("golden legs", 3)]
    return clothes_list[random.randint(0, len(clothes_list)-1)]
