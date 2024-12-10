def possible_trails(matrix, start, target):
    if start == target:
        return 1

    res = 0
    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = start[0] + dx, start[1]+dy
        if (nx, ny) in matrix and matrix[nx, ny] == matrix[start] + 1:
            res += possible_trails(matrix, (nx, ny), target)

    return res


def run():
    output1 = 0
    output2 = 0
    with open('./inputs/day10.txt') as file:
        matrix = {}
        starts = []
        targets = []
        for i, line in enumerate(file):
            for j, char in enumerate(line.strip()):
                matrix[i, j] = int(char)
                if char == '0':
                    starts.append((i, j))
                if char == '9':
                    targets.append((i, j))

    for start in starts:
        for target in targets:
            trails = possible_trails(matrix, start, target)
            output2 += trails
            if trails > 0:
                output1 += 1

    return output1, output2


part1, part2 = run()
print("Part 1: ", part1)
print("Part 2: ", part2)
