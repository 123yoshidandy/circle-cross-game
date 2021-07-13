# coding: utf-8

FIELD_WIDTH, FIELD_HEIGHT = 10, 8
COUNT_MAX = 5
CIRCLE, CROSS, EMPTY = "o", "x", "."


def print_field(field):
    print("\n  " + str(list(range(1, len(field[0]) + 1))).replace("[", "").replace("]", "").replace(",", ""))
    for i, row in enumerate(field):
        print(str(i + 1) + " " + str(row).replace("'", "").replace("[", "").replace("]", "").replace(",", ""))
    print("-" * (2 * len(field[0]) + 1))


def exist_empty(field):
    for row in field:
        if EMPTY in row:
            return True
    return False


def count_stone(field, x, y, dx, dy, mark):
    x, y = x + dx, y + dy
    if 0 <= x < len(field[0]) and 0 <= y < len(field) and field[y][x] == mark:
        return 1 + count_stone(field, x, y, dx, dy, mark)
    else:
        return 0


def main():
    field = [[EMPTY for _ in range(FIELD_WIDTH)] for __ in range(FIELD_HEIGHT)]

    winner = None
    mark = CIRCLE  # first move
    while winner is None and exist_empty(field):
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

        except Exception as error:
            print("ERROR: " + str(error))  # Don't change turn

        else:
            field[y][x] = mark

            count = max(
                1 + count_stone(field, x, y, 1,  0, mark) + count_stone(field, x, y, -1,  0, mark),  # row
                1 + count_stone(field, x, y, 0,  1, mark) + count_stone(field, x, y,  0, -1, mark),  # column
                1 + count_stone(field, x, y, 1,  1, mark) + count_stone(field, x, y, -1, -1, mark),  # down to the right
                1 + count_stone(field, x, y, 1, -1, mark) + count_stone(field, x, y, -1,  1, mark),  # up to the right
            )
            if count >= COUNT_MAX:
                winner = mark

            mark = CROSS if mark == CIRCLE else CIRCLE  # change turn CIRCLE <--> CROSS

    print_field(field)
    if winner:
        print("Winner: '" + winner + "' !!")
    else:
        print("Draw....")


if __name__ == "__main__":
    main()
