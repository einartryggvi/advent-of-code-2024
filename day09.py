def part1():
    output = 0
    with open('./inputs/day09.txt') as file:
        for line in file:
            result = []
            x = 0
            for i, num in enumerate(line.strip()):
                num = int(num)
                if i % 2:
                    result.extend(['.' for i in range(num)])
                else:
                    result.extend([x for i in range(num)])
                    x += 1
            x = len(result) - 1
            for i in range(0, x):
                if result[i] == '.':
                    while result[x] == '.':
                        x -= 1
                    if i > x:
                        break
                    tmp = result[i]
                    result[i] = result[x]
                    result[x] = tmp
                    x -= 1
            for i in range(len(result)):
                if result[i] == '.':
                    break
                output += i * int(result[i])
    return output


class File:
    def __init__(self, file_id, num_blocks):
        self.file_id = file_id
        self.blocks = [str(file_id)] * num_blocks
        self.num_blocks = num_blocks

    def __repr__(self):
        return ''.join(self.blocks)


class FreeSpace:
    def __repr__(self):
        return '.'


def find_free_space(line, count):
    r = 0
    s = -1
    c = 0
    while r < len(line):
        curr = line[r]
        if type(curr) != FreeSpace:
            s = -1
            c = 0
            r += 1
            continue

        c += 1
        if s < 0:
            s = r

        if c == count:
            return s, r+1

        r += 1

    return -1, -1


def part2():
    output = 0
    with open('./inputs/day09.txt') as file:
        line = file.readline().strip()
        result = []
        file_ids = []
        x = 0
        for i, num in enumerate(line):
            num = int(num)
            if i % 2:
                result.extend([FreeSpace() for i in range(num)])
            else:
                result.append(File(x, num))
                file_ids.append(x)
                x += 1

        file_ids.reverse()
        for file_id in file_ids:
            i, f = [(i, f) for i, f in enumerate(result) if type(
                f) == File and f.file_id == file_id][0]
            c = f.num_blocks
            s, e = find_free_space(result, c)
            if s >= 0 and e >= 0 and s < i:
                result[s] = f
                result[i:] = [FreeSpace()]*c + result[i+1:]
                del result[s+1:e]

        blocks = []
        for r in result:
            if type(r) == FreeSpace:
                blocks.append('.')
                continue
            blocks.extend(r.blocks)

        for i, r in enumerate(blocks):
            if r == '.':
                continue
            output += i * int(r)
    return output


print("Part 1: ", part1())
print("Part 2: ", part2())
