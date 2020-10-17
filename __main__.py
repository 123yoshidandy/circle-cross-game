# coding: utf-8


FIELD_SIZE = 8
COUNT_MAX = 5


def print_field(field):
    line = " "
    for i in range(len(field[0])):
        line += " " + str(i + 1)
    print(line)
    for i, row in enumerate(field):
        print(str(i + 1) + " " + str(row).replace("[", "").replace("]", "").replace("'", "").replace(",", ""))


def count_mark(field, mark):
    count = 0
    for row in field:
        for cell in row:
            if cell == mark:
                count += 1
    return count


def count_stone_inner(field, x, y, weight_x, weight_y, mark):
    count = 0
    i = x + weight_x
    j = y + weight_y
    while 0 <= i < len(field[0]) and 0 <= j < len(field) and field[j][i] == mark:
        count += 1
        i += 1 * weight_x
        j += 1 * weight_y
    return count


def count_stone(field, x, y, weight_x, weight_y, mark):
    count = 1  # 座標自身
    count += count_stone_inner(field, x, y,      weight_x,      weight_y, mark)  # プラス方向
    count += count_stone_inner(field, x, y, -1 * weight_x, -1 * weight_y, mark)  # マイナス方向
    return count


def main():
    field = [["." for _ in range(FIELD_SIZE)] for __ in range(FIELD_SIZE)]

    winner = None
    is_circle = True
    while winner is None and count_mark(field, ".") > 0:
        mark = "o" if is_circle else "x"
        print_field(field)
        print("Turn of '" + mark + "' !")
        try:
            point = input("Please input point (x, y): ")
            x, y = point.split(",")
            x, y = int(x) - 1, int(y) - 1
            if field[y][x] != '.':
                raise Exception("This point is already putted !")

            field[y][x] = mark

            count = max(
                count_stone(field, x, y, 1,  0, mark),  # row
                count_stone(field, x, y, 0,  1, mark),  # column
                count_stone(field, x, y, 1,  1, mark),  # down to the right
                count_stone(field, x, y, 1, -1, mark),  # up to the right
            )
            if count >= COUNT_MAX:
                winner = mark

            is_circle = not is_circle  # change turn "o" <--> "x"

        except Exception as error:
            print("ERROR: " + str(error))

    print_field(field)
    print("-----------------")
    if winner:
        print("Winner: '" + winner + "' !!")
    else:
        print("Draw....")


if __name__ == "__main__":
    main()
