import re


def run():
    file = open('./inputs/day17.txt')
    a, b, c, _, r = file.read().split('\n')
    a = int(re.sub(r'([^\-0-9]+)', '', a.strip()))
    b = int(re.sub(r'([^\-0-9]+)', '', b.strip()))
    c = int(re.sub(r'([^\-0-9]+)', '', c.strip()))
    r = [int(rr) for rr in r.split(': ')[1].split(',')]

    output = []
    i = 0
    while i < len(r):
        opcode = r[i]
        operand = r[i+1]
        combo_operand = operand
        if operand == 4:
            combo_operand = a
        elif operand == 5:
            combo_operand = b
        elif operand == 6:
            combo_operand = c

        if opcode == 0:
            a = a // 2**combo_operand
        elif opcode == 1:
            b = b ^ operand
        elif opcode == 2:
            b = int(combo_operand % 8)
        elif opcode == 3:
            if a != 0:
                i = operand
                continue
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            output.append(int(combo_operand % 8))
        elif opcode == 6:
            b = a // 2**combo_operand
        elif opcode == 7:
            c = a // 2**combo_operand
        i += 2

    return ','.join([str(o) for o in output]), 0


part1, part2 = run()
print('Part 1:', part1)
print('Part 2:', part2)
