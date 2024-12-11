def process(cache, iteration, max_iterations, count, num):
    if (iteration, num) in cache:
        return cache[(iteration, num)]

    if iteration == max_iterations:
        return 1

    if num == '0':
        cache[(iteration, num)] = process(
            cache, iteration + 1, max_iterations, count + 1, '1')
    elif len(num) % 2 == 0:
        if len(num) == 1:
            cache[(iteration, num)] = process(
                cache, iteration + 1, max_iterations, count + 1, num)
        else:
            first, second = num[:len(num)//2], num[len(num)//2:]
            second = second.lstrip('0') if len(
                second.lstrip('0')) > 0 else '0'

            cache[(iteration, num)] = process(cache, iteration + 1, max_iterations, count +
                                              1, first) + process(cache, iteration + 1, max_iterations, count + 1, second)
    else:
        new_num = str(int(num)*2024)
        cache[(iteration, num)] = process(
            cache, iteration + 1, max_iterations, count + 1, new_num)

    return cache[(iteration, num)]


def run():
    with open('./inputs/day11.txt') as file:
        numbers = file.readline().strip().split()
        cache = {}
        cache2 = {}
        output1 = 0
        output2 = 0
        for num in numbers:
            output1 += process(cache, 0, 25, 0, num)
            output2 += process(cache2, 0, 75, 0, num)
    return output1, output2


part1, part2 = run()
print("Part 1: ", part1)
print("Part 2: ", part2)
