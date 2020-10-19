# coding: utf-8


FIELD_SIZE = 8
COUNT_MAX = 5
CIRCLE = "o"
CROSS = "x"
EMPTY = "."


def print_field(field):
    line = "\n "
    for i in range(len(field[0])):
        line += " " + str(i + 1)
    print(line)
    for i, row in enumerate(field):
        print(str(i + 1) + " " + str(row).replace("[", "").replace("]", "").replace("'", "").replace(",", ""))
    print("-----------------")


def exist_empty(field):
    for row in field:
        if EMPTY in row:
            return True
    return False


def count_stone(field, x, y, dx, dy, mark):
    x += dx
    y += dy
    if 0 <= x < len(field[0]) and 0 <= y < len(field) and field[y][x] == mark:
        return 1 + count_stone(field, x, y, dx, dy, mark)
    else:
        return 0


def main():
    field = [[EMPTY for _ in range(FIELD_SIZE)] for __ in range(FIELD_SIZE)]

    winner = None
    is_circle = True
    while winner is None and exist_empty(field):
        mark = CIRCLE if is_circle else CROSS
        print_field(field)
        print("Turn of '" + mark + "' !")
        try:
            point = input("Please input point (x, y): ")
            x, y = point.split(",")
            x, y = int(x) - 1, int(y) - 1
            if not (0 <= x < len(field[0])) or not (0 <= y < len(field)):
                raise Exception("This point is out of field !")
            if field[y][x] != EMPTY:
                raise Exception("This point is already putted !")

            field[y][x] = mark

            count = max(
                1 + count_stone(field, x, y, 1,  0, mark) + count_stone(field, x, y, -1,  0, mark),  # row
                1 + count_stone(field, x, y, 0,  1, mark) + count_stone(field, x, y,  0, -1, mark),  # column
                1 + count_stone(field, x, y, 1,  1, mark) + count_stone(field, x, y, -1, -1, mark),  # down to the right
                1 + count_stone(field, x, y, 1, -1, mark) + count_stone(field, x, y, -1,  1, mark),  # up to the right
            )
            if count >= COUNT_MAX:
                winner = mark

        except Exception as error:
            print("ERROR: " + str(error))

        else:
            is_circle = not is_circle  # change turn CIRCLE <--> CROSS

    print_field(field)
    if winner:
        print("Winner: '" + winner + "' !!")
    else:
        print("Draw....")


if __name__ == "__main__":
    main()
