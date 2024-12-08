from collections import defaultdict
from utils import manhattan_distance, points_collinear


def run():
    with open('./inputs/day08.txt') as file:
        matrix = {}
        antenna_map = defaultdict(list)
        for i, line in enumerate(file):
            for j, char in enumerate(line.strip()):
                matrix[i, j] = char
                if char != '.':
                    antenna_map[char].append((i, j))

    p1 = set()
    p2 = set()

    for point in matrix:
        for antennas in antenna_map.values():
            for a1 in antennas:
                for a2 in antennas:
                    if a1 != a2:
                        distance1 = manhattan_distance(point, a1)
                        distance2 = manhattan_distance(point, a2)

                        # If a1 and a2 have the same slope compared to the candiate point they are on the same line
                        if points_collinear(point, a1, a2):
                            p2.add(point)

                            # The canditate point is valid if one of the antenna points is twice the distance from the it compared to the other antenna point
                            if distance1 == distance2*2 or distance1*2 == distance2:
                                p1.add(point)

    return len(p1), len(p2)


part1, part2 = run()

print("Part 1: ", part1)
print("Part 2: ", part2)
