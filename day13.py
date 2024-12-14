import re


def parse_xy(s):
    m = re.match(r'.*X(\+|=)([0-9]+), Y(\+|=)([0-9]+).*', s)
    return int(m.group(2)), int(m.group(4))


def brute_force(a, b, p):
    for i in range(100):
        for j in range(100):
            if (a[0] * i + b[0] * j, a[1] * i + b[1] * j) == p:
                return 3 * i + j
    return 0


def run():
    with open('./inputs/day13-test.txt') as file:
        machines = file.read().split('\n\n')
        output = 0
        output2 = 0
        for m in machines:
            a, b, p = [parse_xy(abp) for abp in m.strip().split('\n')]
            p2 = (10000000000000 + p[0], 10000000000000 + p[1])
            output += brute_force(a, b, p)
        return output, output2


part1, part2 = run()
print('Part 1:', part1)
print('Part 2:', part2)
