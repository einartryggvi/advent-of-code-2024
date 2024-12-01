def part1():
    total_dist = 0

    with open('./inputs/day01.txt') as file:
        list1 = []
        list2 = []
        for line in file:
            first, second = line.split()
            list1.append(int(first))
            list2.append(int(second))
        list1.sort()
        list2.sort()

        for i, _ in enumerate(list1):
            first, second = list1[i], list2[i]
            total_dist += abs(int(second) - int(first))

    return total_dist


def part2():
    res = 0

    with open('./inputs/day01.txt') as file:
        list1 = []
        list2 = []
        for line in file:
            first, second = line.split()
            list1.append(int(first))
            list2.append(int(second))

        for i, _ in enumerate(list1):
            num = list1[i]
            count = list2.count(num)
            res += num * count

    return res


print("Part 1: ", part1())
print("Part 2: ", part2())
