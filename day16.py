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
    prev = defaultdict(list)

    while queue:
        cost, p, d = heapq.heappop(queue)

        visited_state = (p, d)
        if visited_state in visited and visited[visited_state] <= cost:
            continue
        visited[visited_state] = cost

        for nd in next_directions(d):
            np = (p[0] + nd[0], p[1] + nd[1])
            if not np in matrix:
                continue

            if matrix[np] == '#':
                queue.append((cost + 1001, p, nd))
                continue

            if nd != d:
                queue.append((cost + 1001, np, nd))
                prev[np, nd, cost+1001].append((p, d, cost))
            else:
                queue.append((cost + 1, np, nd))
                prev[np, nd, cost+1].append((p, d, cost))

    return prev


def end_states(prev, e):
    options = []
    for a in prev.values():
        options.extend([(p, d, c)
                        for p, d, c in a if p == e])

    cost = min([o[2] for o in options])
    return [o for o in options if o[2] == cost]


def all_paths(prev, s, cost, states):
    path = []
    while states:
        options = []
        for ps in states:
            options.extend([b for b in prev[ps] if b[2] < cost])
        tiles = [s[0] for s in options]
        path.extend(tiles)
        if s in tiles:
            break
        states = options
    return set(path)


def run():
    file = open('./inputs/day16.txt')
    matrix = {}
    for y, line in enumerate(file):
        for x, char in enumerate(line.strip()):
            matrix[x, y] = char

    s = [(x, y) for (x, y), char in matrix.items() if char == 'S'][0]
    e = [(x, y) for (x, y), char in matrix.items() if char == 'E'][0]
    matrix[s] = '.'
    matrix[e] = '.'

    prev = min_cost_path(matrix, s, (0, 1), e)

    es = end_states(prev, e)
    cost = es[0][2]
    path = all_paths(prev, s, cost, es)

    return cost - 1001, len(path) + 1


part1, part2 = run()
print('Part 1:', part1)
print('Part 2:', part2)
