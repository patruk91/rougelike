


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
    map_level = [["@", " ", " ", " ", " ", ], [" ", " ", " ", " ", " ", ], [" ", " ", " ", " ", " ", ], [" ", " ", " ", " ", " ", ] ,[" ", " ", " ", " ", " ", ]]
    print(map_level)
    while True:
        # hero_indice = [column, row]
        get_char = get_char_in_terminal()
        if get_char == "d":
            MOVE_RIGHT = 1
            map_level = move_horizontally(map_level, MOVE_RIGHT)
        elif get_char == "a":
            MOVE_LEFT = -1
            map_level = move_horizontally(map_level, MOVE_LEFT)
        elif get_char == "w":
            MOVE_UP = -1
            move_vertically(map_level, MOVE_UP)
        elif get_char == "s":
            MOVE_DOWN = 1
            move_vertically(map_level, MOVE_DOWN)

        if get_char == "q":
            exit()


def move_horizontally(map_level, move):
    hero_position = get_hero_position(map_level)
    x_position = hero_position[0]
    y_position = hero_position[1]
    map_level[y_position][x_position] = " "

    # update position in list
    x_position += move
    map_level[y_position][x_position] = "@"
    print_some(map_level)
    return map_level


def move_vertically(map_level, move):
    hero_position = get_hero_position(map_level)
    x_position = hero_position[0]
    y_position = hero_position[1]
    map_level[y_position][x_position] = " "

    # update position in list
    y_position += move
    map_level[y_position][x_position] = "@"
    print_some(map_level)
    return map_level


def get_hero_position(map_level):
    position = [[line.index("@"), map_level.index(line)] for line in map_level if "@" in line][0]
    print(position)
    return position


def print_some(level):
    for line in level:
        print(line)

# x = get_char_in_terminal()
# print(x)
print(movement())