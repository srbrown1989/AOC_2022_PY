# part 1: read from file, strip each line, continue to sum each line until hit empty string(as \n removed)
# add this sum to list.
elves = []

current_sum = 0

with open("data.txt") as file:
    for line in file:
        current = line.strip()
        if current == "":
            elves.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(current)
print(max(elves))  # result of part 1.

# part 2, use max to get top value, remove from list, repeat until have top 3.

top_elves = []
for x in range(1, 4):
    top_elf = max(elves)
    top_elves.append(top_elf)
    elves.remove(top_elf)

print(sum(top_elves))  # result of part 2.

# most interesting solution to me found on reddit.
# with open("startpos.txt") as file:
#    data = [[int(y) for y in x.splitlines()] for x in file.read().split("\n\n")]
#    sorted_data = sorted(sum(x) for x in data)
#    print(max(sorted_data))
#    print(sum(sorted_data[-3:]))
