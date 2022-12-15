import numpy as np

with open('data.txt', 'r') as f:
    lines = f.readlines()
    movements = [(entry.strip().split(' ')[0],
                  int(entry.strip().split(' ')[1])
                  )
                 for entry in lines]
head = np.array([0, 0])
tail = np.array([0, 0])


def update_tail(head, tail):
    difference = head - tail
    change_for_tail = {
        # head is 2 up 1 right from tail, then tail follows up and right once
        (2, 1): (1, 1),
        # 1 up, 2 right
        (1, 2): (1, 1),
        # 2up
        (2, 0): (1, 0),
        # 2up 1left
        (2, -1): (1, -1),
        # 1up, 2eft
        (1, -2): (1, -1),
        # 2left
        (0, -2): (0, -1),
        (-1, -2): (-1, -1),
        (-2, -1): (-1, -1),
        (-2, 0): (-1, 0),
        (-2, 1): (-1, 1),
        (-1, 2): (-1, 1),
        (0, 2): (0, 1),
        # additional cases for part 2
        (2, 2): (1, 1),
        (-2, -2): (-1, -1),
        (-2, 2): (-1, 1),
        (2, -2): (1, -1)
    }
    new_tail_pos = tail + np.array(change_for_tail.get(tuple(difference), (0, 0)))
    return new_tail_pos


def update_head(head, direction):
    if direction == 'R':
        head[1] += 1
    elif direction == 'L':
        head[1] -= 1
    elif direction == 'U':
        head[0] += 1
    elif direction == 'D':
        head[0] -= 1
    return head

# Part 1.
# tail_positions = set([tuple(tail)])
# for direction, distance in movements:
#     while distance > 0:
#         head = update_head(head, direction)
#         distance -= 1
#         tail = update_tail(head, tail)
#         tail_positions.add(tuple(tail))
# len(tail_positions)

rope = [np.array([0, 0]) for _ in range(10)]

tail_positions = set(tuple(rope[9]))
for direction, distance in movements:
    while distance > 0:
        rope[0] = update_head(rope[0], direction)
        distance -= 1
        for i in range(1, len(rope)):
            rope[i] = update_tail(rope[i-1], rope[i])
        tail_positions.add(tuple(rope[9]))
print(len(tail_positions) - 1)