


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
    level = [["@", " ", " ", " ", " ", ], [" ", " ", " ", " ", " ", ]] + [[" ", " ", " ", " ", " ", ]] * 3
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
        elif get_char == "w":
            MOVE_UP = -1
            move_vertically(level, MOVE_UP)
        elif get_char == "s":
            MOVE_DOWN = 1
            move_vertically(level, MOVE_DOWN)

        if get_char == "q":
            exit()


def move_horizontally(level, move):
    position = [[line.index("@"), level.index(line)] for line in level if "@" in line][0]
    hero_horizontal_position = position[0] + move
    for horizontal in level:
        if "@" in horizontal:
            for indice in range(len(horizontal)):
                horizontal[indice] = " "
                horizontal[hero_horizontal_position] = "@"
    print(level)
    return level


def move_vertically(level, move):
    position = [[line.index("@"), level.index(line)] for line in level if "@" in line][0]
    level[position[1]][position[0]] = " "
    position[1] += move
    level[position[1]][position[0]] = "@"
    print(level)





# x = get_char_in_terminal()
# print(x)
print(movement())