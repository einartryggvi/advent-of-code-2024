def levels_diff(levels):
    return [int(levels[i])-int(levels[i+1])
            for i in range(len(levels) - 1)]


def monotonic_increasing(diff, lower, upper):
    return all([n <= upper and n > lower for n in diff])


def monotonic_decreasing(diff, lower, upper):
    return all([n >= upper and n < lower for n in diff])


def part1():
    total = 0

    with open('./inputs/day02.txt') as file:
        for line in file:
            levels = line.split()
            diff = levels_diff(levels)
            increasing = monotonic_increasing(diff, 0, 3)
            decreasing = monotonic_decreasing(diff, 0, -3)

            if increasing or decreasing:
                total += 1

    return total


def part2():
    total = 0

    with open('./inputs/day02.txt') as file:
        for line in file:
            levels = line.split()
            levels_variations = [levels] + [levels[:l] + levels[l+1:]
                                            for l in range(0, len(levels))]
            for lv in levels_variations:
                diff = levels_diff(lv)
                increasing = monotonic_increasing(diff, 0, 3)
                decreasing = monotonic_decreasing(diff, 0, -3)

                if increasing or decreasing:
                    total += 1
                    break

    return total


print("Part 1: ", part1())
print("Part 2: ", part2())
