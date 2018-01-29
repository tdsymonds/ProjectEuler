def main():
    # get the triangle
    triange = get_triangle()

    # loop through each of the rows
    for i, row in enumerate(triange):
        if i == 0:
            # if it's the first row then the max
            # possible values is the row
            max_row = row
        else:
            new_max_row = []
            # for each number in the list, what's the maximum possible path
            # from the previous row?
            # Append the results to the new max row variable.
            for j, num in enumerate(row):
                new_max_row.append(num + max(max_row[j], max_row[j+1]))

            # update the max row with the new max row.
            max_row = new_max_row

    # print the max possible path.
    print(max_row[0])


def get_triangle():
    """
    Returns the text triangle as a list of lists from bottom
    the bottom of the triangle up.
    """
    triange_str = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
    triange = []
    rows = triange_str.split('\n')
    for row in reversed(rows):
        triange.append(list(map(int, row.split(' '))))
    return triange


if __name__ == "__main__":
    main()
