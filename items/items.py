import random


def weapons():
    weapons_list = [("dagger", 2), ("axe", 3), ("pick", 3), ("stick", 1),
                    ("infinity edge", 15), ("bloodrazor", 10)]
    return weapons_list[random.randint(0, len(weapons_list)-1)]


def food():
    food_list = [("ham", 6), ("meat", 4), ("melon", 2), ("apple", 1),
                 ("cake", 5), ("sweets", 2)]
    return food_list[random.randint(0, len(food_list)-1)]


def clotches():
    clothes_list = [("brass helmet", 3), ("rainbow shield", 15),
                    ("doran shield", 2), ("plate armor", 5),
                    ("steel boots", 4), ("golden legs", 8)]
    return clothes_list[random.randint(0, len(clothes_list)-1)]

