
from itertools import product


def matches_total_recursive(total, agg, numbers):
    if len(numbers) == 0:
        return total == agg

    if agg > total:
        return False

    num = numbers[0]

    s = matches_total_recursive(total, agg + num, numbers[1:])
    m = matches_total_recursive(total, agg * num, numbers[1:])

    return s or m


def matches_total(total, numbers):
    combs = product('+*',  repeat=len(numbers)-1)
    for c in combs:
        tmp = numbers[0]
        for i, op in enumerate(c):
            if op == '+':
                tmp += numbers[i+1]
            if op == '*':
                tmp *= numbers[i+1]
            if tmp > total:
                break

        if tmp == total:
            return True

    return False


def matches_total_with_concat_recursive(total, agg, numbers):
    if len(numbers) == 0:
        return total == agg

    if agg > total:
        return False

    num = numbers[0]

    s = matches_total_with_concat_recursive(total, agg + num, numbers[1:])
    m = matches_total_with_concat_recursive(total, agg * num, numbers[1:])
    c = matches_total_with_concat_recursive(
        total, int(str(agg) + str(num)), numbers[1:])

    return s or m or c


def matches_total_with_concat(total, numbers):
    combs = product('+*|', repeat=len(numbers)-1)
    for c in combs:
        tmp = numbers[0]
        for i, op in enumerate(c):
            if op == '+':
                tmp += numbers[i+1]
            if op == '*':
                tmp *= numbers[i+1]
            if op == '|':
                tmp = int(str(tmp) + str(numbers[i+1]))
            if tmp > total:
                break

        if tmp == total:
            return True

    return False


def run():
    part1, part2 = 0, 0
    with open('./inputs/day07.txt') as file:
        for line in file:
            total, rest = line.strip().split(': ')
            total = int(total)
            numbers = [int(n) for n in rest.split()]
            if matches_total_recursive(total, 0, numbers):
                part1 += total
                continue
            if matches_total_with_concat_recursive(total, 0, numbers):
                part2 += total
    return part1, part2


part1, part2 = run()
print("Part 1: ", part1)
print("Part 2: ", part2)
