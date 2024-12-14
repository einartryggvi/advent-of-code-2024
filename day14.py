
from collections import defaultdict
import re


def parse(s):
    m = re.match(r'.*p=([0-9]+),([0-9]+) v=([0-9\-]+),([0-9\-]+).*', s)
    return (int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))


def quadrant(cx, cy, x, y):
    if (x > cx and y > cy):
        return 1
    elif (x < cx and y > cy):
        return 2
    elif (x < cx and y < cy):
        return 3
    elif (x > cx and y < cy):
        return 4


def part1():
    with open('./inputs/day14.txt') as file:
        maxX = 101
        maxY = 103
        output = 1
        counts = defaultdict(int)
        robots = []
        for line in file:
            p, v = parse(line.strip())
            robots.append((p, v))

        for i in range(100):
            counts.clear()
            for i, (p, v) in enumerate(robots):
                (x, y) = p
                (vx, vy) = v
                nx, ny = x + vx, y + vy
                if nx < 0:
                    nx = maxX + nx
                if ny < 0:
                    ny = maxY + ny
                if nx >= maxX:
                    nx = nx - maxX
                if ny >= maxY:
                    ny = ny - maxY
                counts[nx, ny] += 1
                robots[i] = ((nx, ny), v)
        center = (maxX//2, maxY//2)
        quadrant_counts = defaultdict(int)
        for (x, y), c in counts.items():
            q = quadrant(center[0], center[1], x, y)
            if q:
                quadrant_counts[q] += c
        for c in quadrant_counts.values():
            output *= c
        return output


def part2():
    with open('./inputs/day14.txt') as file:
        maxX = 101
        maxY = 103
        counts = defaultdict(int)
        robots = []
        for line in file:
            p, v = parse(line.strip())
            robots.append((p, v))

        for iteration in range(maxX * maxY):
            counts.clear()
            for i, (p, v) in enumerate(robots):
                (x, y) = p
                (vx, vy) = v
                nx, ny = x + vx, y + vy
                if nx < 0:
                    nx = maxX + nx
                if ny < 0:
                    ny = maxY + ny
                if nx >= maxX:
                    nx = nx - maxX
                if ny >= maxY:
                    ny = ny - maxY
                counts[nx, ny] += 1
                robots[i] = ((nx, ny), v)
            robot_fields = counts.keys()
            for y in range(maxY):
                s = ''
                for x in range(maxX):
                    s += 'S' if (x, y) in robot_fields else '.'
                if 'SSSSSSSS' in s:
                    return iteration + 1
        return 0


print("Part 1: ", part1())
print("Part 1: ", part2())
