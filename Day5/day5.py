from collections import deque

stacks = [deque() for x in range(9)]

with open("startpos.txt") as start:
    for i in range(9):
        current = list(start.readline().strip())
        for crate in current:
            stacks[i].append(crate)


def make_one_move(instruct):
    n = instruct[0]
    strt = instruct[1]-1
    fin = instruct[2]-1
    for x in range(n):
        stacks[fin].append(stacks[strt].pop())


def make_multiple_move(instruct):
    order = deque()
    n = instruct[0]
    strt = instruct[1] - 1
    fin = instruct[2] - 1
    for x in range(n):
        order.append(stacks[strt].pop())
    for x in range(n):
        stacks[fin].append(order.pop())


with open("instructions.txt") as instructions:
    for line in instructions:
        instruction = [int(s) for s in line.split() if s.isdigit()]
        if instruction[0] == 1:
            make_one_move(instruction)
        else:
            make_multiple_move(instruction)

final_positions = ""
for i in range(9):
    x = stacks[i].pop()
    final_positions += x

print(f"Part 2: {final_positions}")
