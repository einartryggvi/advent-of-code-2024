from collections import defaultdict
import heapq


def next_directions(current_direction):
    if current_direction == (-1, 0):
        return [(-1, 0), (0, 1), (0, -1)]
    elif current_direction == (1, 0):
        return [(1, 0), (0, 1), (0, -1)]
    elif current_direction == (0, -1):
        return [(0, -1), (1, 0), (-1, 0)]
    elif current_direction == (0, 1):
        return [(0, 1), (1, 0), (-1, 0)]
    else:
        return [(-1, 0), (1, 0), (0, -1), (0, 1)]


def min_cost_path(matrix, sp, sd, tp):
    queue = [(0, sp, sd)]
    visited = {}

    while queue:
        cost, p, d = heapq.heappop(queue)

        visited_state = (p, d)
        if visited_state in visited and visited[visited_state] <= cost:
            continue
        visited[visited_state] = cost

        if p == tp:
            return cost

        for nd in next_directions(d):
            np = (p[0] + nd[0], p[1] + nd[1])
            if not np in matrix or matrix[np] == '#':
                continue

            queue.append((cost + 1, np, nd))

    return 10**6


def run():
    file = open('./inputs/day18.txt')
    matrix = {}
    X = 71
    Y = 71
    B = 1024
    for y in range(Y):
        for x in range(X):
            matrix[x, y] = '.'

    falling_bytes = [(int(line.split(',')[0]), int(line.split(',')[1]))
                     for line in file]

    for i in range(0, B):
        matrix[falling_bytes[i]] = '#'

    part1 = min_cost_path(matrix, (0, 0), (0, 1), (X-1, Y-1))

    for i in range(B, len(falling_bytes)):
        matrix[falling_bytes[i]] = '#'
        if min_cost_path(matrix, (0, 0), (0, 1), (X-1, Y-1)) == 10**6:
            x, y = falling_bytes[i]
            part2 = f'{x},{y}'
            break

    return part1, part2


part1, part2 = run()
print('Part 1:', part1)
print('Part 2:', part2)
