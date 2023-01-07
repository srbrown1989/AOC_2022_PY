from copy import deepcopy

with open("data.txt") as file:
    raw_data = file.read().strip()
    raw_pairs = raw_data.split("\n\n")


def compare(first, second):
    while len(first) > 0 and len(second) > 0:
        left = first.pop(0)
        right = second.pop(0)
        if type(left) == int and type(right) == int:
            if left < right:
                return 1
            elif left > right:
                return -1
        if type(left) == list and type(right) == list:
            sub_comparison = compare(left, right)
            if sub_comparison != 0:
                return sub_comparison
        if type(left) == int and type(right) == list:
            sub_comparison = compare(list([left]), right)
            if sub_comparison != 0:
                return sub_comparison
        if type(left) == list and type(right) == int:
            sub_comparison = compare(left, list([right]))
            if sub_comparison != 0:
                return sub_comparison
    if len(first) < len(second):
        return 1
    elif len(first) > len(second):
        return -1
    else:
        return 0


correct_orders = []
def solve_1():
    for x in range(0, len(raw_pairs)):
        pair = raw_pairs[x].split("\n")
        left = eval(pair[0])
        right = eval(pair[1])
        if compare(left, right) == 1:
            correct_orders.append(x+1)

    print(sum(correct_orders))

def solve_2():
        with open("data.txt", 'r') as f:
            lines = f.readlines()
            lines = [entry.strip() for entry in lines]

        smaller_than_2 = 0
        smaller_than_6 = 0
        while len(lines) > 0:
            line = lines.pop(0)
            if len(line) == 0:
                continue
            list_from_file = eval(line)

            if compare(deepcopy(list_from_file), [[2]]) == 1:
                smaller_than_2 += 1
            if compare(deepcopy(list_from_file), [[6]]) == 1:
                smaller_than_6 += 1

        position_of_2 = smaller_than_2 + 1
        position_of_6 = smaller_than_6 + 2
        print(f"{position_of_2=}, {position_of_6=}")
        print(position_of_2 * position_of_6)

solve_1()
solve_2()