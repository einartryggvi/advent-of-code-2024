def verify_update(rules, pages):
    for i, page in enumerate(pages):
        for first, second in rules:
            if first == page and second in pages and i > pages.index(second):
                return False
    return True


def part1():
    total = 0

    with open('./inputs/day05.txt') as file:
        rules, updates = file.read().split('\n\n')
        rules = [(r.split('|')[0], r.split('|')[1]) for r in rules.split()]
        for update in updates.split():
            pages = update.split(',')
            if verify_update(rules, pages):
                total += int(pages[len(pages)//2])

    return total


def order_pages(rules, pages):
    applicable_rules = [(first, second) for first,
                        second in rules if first in pages and second in pages]

    while True:
        changed = False
        for first, second in applicable_rules:
            if pages.index(first) < pages.index(second):
                changed = True
                tmp = pages[pages.index(second)]
                pages[pages.index(second)] = pages[pages.index(first)]
                pages[pages.index(first)] = tmp

        if not changed:
            break

    return pages


def part2():
    total = 0

    with open('./inputs/day05.txt') as file:
        rules, updates = file.read().split('\n\n')
        rules = [(r.split('|')[0], r.split('|')[1]) for r in rules.split()]
        for update in updates.split():
            pages = update.split(',')
            if not verify_update(rules, pages):
                ordered_pages = order_pages(rules, pages)
                total += int(pages[len(ordered_pages)//2])

    return total


print("Part 1: ", part1())
print("Part 2: ", part2())
