def next_direction(current_direction):
    if current_direction == (-1, 0):
        return (0, 1)
    elif current_direction == (1, 0):
        return (0, -1)
    elif current_direction == (0, -1):
        return (-1, 0)
    elif current_direction == (0, 1):
        return (1, 0)


def part1():
    with open('./inputs/day06.txt') as file:
        matrix = {}
        point = (0, 0)
        visited = []
        direction = (0, 0)
        for i, line in enumerate(file):
            for j, char in enumerate(line.strip()):
                if char in ['^', 'v', '>', '<']:
                    point = (i, j)
                if char == '^':
                    direction = (-1, 0)
                elif char == 'v':
                    direction = (1, 0)
                elif char == '<':
                    direction = (0, -1)
                elif char == '>':
                    direction = (0, 1)
                matrix[i, j] = char

        while True:
            try:
                visited.append(point)
                next_point = point[0] + direction[0], point[1] + direction[1]
                if matrix[next_point] == '#':
                    direction = next_direction(direction)
                    next_point = point[0] + \
                        direction[0], point[1] + direction[1]
                point = next_point
            except:
                break

    return len(set(visited))


def is_cycle(matrix, initial_point, initial_direction):
    visited = []
    point = initial_point
    direction = initial_direction
    while True:
        if not point in matrix:
            return False

        next_point = point[0] + direction[0], point[1] + direction[1]

        while next_point in matrix and matrix[next_point] == '#':
            if (next_point, direction) in visited:
                return True
            visited.append((next_point, direction))
            direction = next_direction(direction)
            next_point = point[0] + \
                direction[0], point[1] + direction[1]
        point = next_point


def part2():
    with open('./inputs/day06.txt') as file:
        matrix = {}
        initial_point = (0, 0)
        visited = []
        initial_direction = (0, 0)
        for i, line in enumerate(file):
            for j, char in enumerate(line.strip()):
                if char in ['^', 'v', '>', '<']:
                    initial_point = (i, j)
                if char == '^':
                    initial_direction = (-1, 0)
                elif char == 'v':
                    initial_direction = (1, 0)
                elif char == '<':
                    initial_direction = (0, -1)
                elif char == '>':
                    initial_direction = (0, 1)
                matrix[i, j] = char

        point = initial_point
        direction = initial_direction
        while True:
            if not point in matrix:
                break

            visited.append(point)

            next_point = point[0] + direction[0], point[1] + direction[1]
            while next_point in matrix and matrix[next_point] == '#':
                direction = next_direction(direction)
                next_point = point[0] + \
                    direction[0], point[1] + direction[1]
            point = next_point

    obstructions = []
    for (i, j) in set(visited):
        new_matrix = matrix.copy()
        new_matrix[i, j] = '#'
        if is_cycle(new_matrix, initial_point, initial_direction):
            obstructions.append((i, j))

    return len(set(obstructions))


print("Part 1: ", part1())
print("Part 2: ", part2())
