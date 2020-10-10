# coding: utf-8


def print_field(field):
    line = " "
    for i in range(len(field[0])):
        line += " " + str(i + 1)
    print(line)
    for i, row in enumerate(field):
        print(str(i + 1) + " " + str(row).replace("[", "").replace("]", "").replace("'", "").replace(",", ""))


def count_stone(field, x, y, weight_x, weight_y, mark):
    count = 1
    i = x + 1 * weight_x
    j = y + 1 * weight_y
    while 0 <= i < len(field[0]) and 0 <= j < len(field) and field[j][i] == mark:
        count += 1
        i += 1 * weight_x
        j += 1 * weight_y
    i = x - 1 * weight_x
    j = y - 1 * weight_y
    while 0 <= i < len(field[0]) and 0 <= j < len(field) and field[j][i] == mark:
        count += 1
        i -= 1 * weight_x
        j -= 1 * weight_y
    print(count)
    return count


def main():
    field = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    num = 3

    is_circle = True
    while True:
        print_field(field)
        print("Turn of '" + ("o" if is_circle else "x") + "' !")
        try:
            point = input("Please input point (x, y): ")
            x, y = point.split(",")
            x, y = int(x) - 1, int(y) - 1
            if field[y][x] != '.':
                raise Exception("This point is already putted !")
            field[y][x] = "o" if is_circle else "x"

            count = max(
                count_stone(field, x, y, 1,  0, "o" if is_circle else "x"),
                count_stone(field, x, y, 0,  1, "o" if is_circle else "x"),
                count_stone(field, x, y, 1,  1, "o" if is_circle else "x"),
                count_stone(field, x, y, 1, -1, "o" if is_circle else "x"),
            )
            if count >= num:
                break

            is_circle = not is_circle
        except Exception as error:
            print("ERROR: " + str(error))

    print_field(field)
    print("----------------")
    print("Winner: '" + ("o" if is_circle else "x") + "' !!")


if __name__ == "__main__":
    main()
