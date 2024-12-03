import re


def part1():
    total = 0

    with open('./inputs/day03.txt') as file:
        for line in file:
            for match in re.finditer(r'mul\([0-9]+,[0-9]+\)', line):
                out = re.match(
                    r'mul\(([0-9]+),([0-9]+)\)', match[0])
                first, second = out[1], out[2]
                total += int(first) * int(second)

    return total


def part2():
    total = 0

    with open('./inputs/day03.txt') as file:
        active = True
        for line in file:
            for match in re.finditer(r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)', line):
                if match[0] == 'do()':
                    active = True
                    continue
                elif match[0] == 'don\'t()':
                    active = False
                    continue

                if active == False:
                    continue

                out = re.match(
                    r'mul\(([0-9]+),([0-9]+)\)', match[0])
                first, second = out[1], out[2]
                total += int(first) * int(second)

    return total


print("Part 1: ", part1())
print("Part 2: ", part2())
