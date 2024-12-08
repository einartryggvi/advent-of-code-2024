
from collections import Counter


def traverse_direction(matrix, i, j, di, dj):
    markers = []
    try:
        antenna1pos = (i + di, j + dj)
        antenna2pos = (
            i + di * 2, j + dj * 2)

        if matrix[antenna1pos] != '.' and matrix[antenna1pos] == matrix[antenna2pos] and matrix[i, j] != matrix[antenna1pos]:
            if (antenna2pos[0] + di, antenna2pos[1] + dj) in matrix:
                end_marker = (antenna2pos[0] + di,
                              antenna2pos[1] + dj)
                markers.append(end_marker)
            markers.append((i, j))
    except:
        pass

    return markers


def process_field(matrix, directions, i, j):
    markers = []
    for di, dj in directions:
        if i + di < 0 or j + dj < 0:
            continue
        markers.extend(traverse_direction(matrix, i, j, di, dj))
    return markers


def part1():
    with open('./inputs/day08.txt') as file:
        matrix = {}
        num_cols = 0
        num_rows = 0
        for i, line in enumerate(file):
            num_cols = i
            for j, char in enumerate(line.strip()):
                num_rows = i
                matrix[i, j] = char

    directions = []
    for di in range(-num_cols, num_cols):
        for dj in range(-num_rows, num_rows):
            directions.append((di, dj))

    markers = []
    for (i, j) in matrix.keys():
        markers.extend(process_field(matrix, directions, i, j))

    return len(set(markers))


def traverse_direction2(matrix, i, j, di, dj):
    if di == 0 and dj == 0:
        return []

    currI = i
    currJ = j

    fields = []
    antennas = []
    while True:
        try:
            if matrix[currI, currJ] != '.':
                antennas.append(matrix[currI, currJ])
            fields.append((currI, currJ))
            currI += di
            currJ += dj
        except:
            break

    valid = [a for a in Counter(antennas).values() if a >= 2]
    if len(valid) > 0:
        return fields
    return []


def process_field2(matrix, directions, i, j):
    markers = []
    for di, dj in directions:
        if i + di < 0 or j + dj < 0:
            continue
        markers.extend(traverse_direction2(matrix, i, j, di, dj))
    return markers


def part2():
    with open('./inputs/day08.txt') as file:
        matrix = {}
        num_cols = 0
        num_rows = 0
        for i, line in enumerate(file):
            num_cols = i
            for j, char in enumerate(line.strip()):
                num_rows = i
                matrix[i, j] = char

    directions = []
    for di in range(num_cols):
        for dj in range(-num_rows, num_rows):
            directions.append((di, dj))

    markers = []
    for (i, j) in matrix.keys():
        markers.extend(process_field2(matrix, directions, i, j))

    return len(set(markers))


print("Part 1: ", part1())
print("Part 2: ", part2())
