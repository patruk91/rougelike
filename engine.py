


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
            level = move_right(level)
        if get_char == "q":
            exit()


def move_right(level):
    hero_indice = [[line.index("@"), level.index(line)] for line in level if "@" in line][0]
    hero_indice[0] += 1
    for line in level:
        for i in range(len(line)):
            if line[i] == "@":
                line[i] = " "
                line[hero_indice[0]] = "@"
            else:
                line[i] = " "
        print(level)
        return level
# x = get_char_in_terminal()
# print(x)
print(movement())