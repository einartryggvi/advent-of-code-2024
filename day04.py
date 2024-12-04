def part1():
    total = 0
    matrix = {}

    with open('./inputs/day04.txt') as file:
        for i, line in enumerate(file):
            for j, char in enumerate(line):
                matrix[i, j] = char

        options = [
            (0, 0),
            (0, 1),
            (1, 0),
            (1, 1),
            (0, -1),
            (-1, 0),
            (-1, -1),
            (-1, 1),
            (1, -1),
        ]

        for (i, j) in matrix:
            for (x, y) in options:
                try:
                    word = matrix[i, j] + matrix[i + (x*1), j + (y*1)] + \
                        matrix[i + (x*2), j + (y*2)] + \
                        matrix[i + (x*3), j + (y*3)]
                    if word == 'XMAS':
                        total += 1
                except:
                    pass

    return total


def is_match(matrix, i, j, option):
    for (x, y), char in option.items():
        if matrix[i + x, j + y] != char:
            return False

    return True


def part2():
    total = 0
    matrix = {}

    with open('./inputs/day04.txt') as file:
        for i, line in enumerate(file):
            for j, char in enumerate(line):
                matrix[i, j] = char

        options = [
            {(-1, -1): 'M', (-1, 1): 'M', (1, -1): 'S', (1, 1): 'S'},
            {(-1, -1): 'S', (-1, 1): 'S', (1, -1): 'M', (1, 1): 'M'},
            {(-1, -1): 'S', (-1, 1): 'M', (1, -1): 'S', (1, 1): 'M'},
            {(-1, -1): 'M', (-1, 1): 'S', (1, -1): 'M', (1, 1): 'S'},
        ]

        for (i, j) in matrix:
            try:
                if matrix[i, j] == 'A':
                    for option in options:
                        if is_match(matrix, i, j, option):
                            total += 1
            except:
                pass

    return total


print("Part 1: ", part1())
print("Part 2: ", part2())
