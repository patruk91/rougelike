


def get_char_in_terminal():
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return char


def movement():
    level = [["@", " ", " ", " ", " ", ], [" ", " ", " ", " ", " ", ]]  # + [[" ", " ", " ", " ", " ", ]] * 10
    print(level)
    while True:
        # hero_indice = [column, row]
        get_char = get_char_in_terminal()
        if get_char == "d":
            MOVE_RIGHT = 1
            level = move_horizontally(level, MOVE_RIGHT)
        elif get_char == "a":
            MOVE_LEFT = -1
            level = move_horizontally(level, MOVE_LEFT)
        if get_char == "q":
            exit()


def move_horizontally(level, move):
    hero_indice = [[line.index("@"), level.index(line)] for line in level if "@" in line][0]
    updated_hero_indice = hero_indice[0] + move
    for horizontal in level:
        if "@" in horizontal:
            for indice in range(len(horizontal)):
                horizontal[indice] = " "
                horizontal[updated_hero_indice] = "@"

    print(level)
    return level
# x = get_char_in_terminal()
# print(x)
print(movement())