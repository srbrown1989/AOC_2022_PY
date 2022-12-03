import string

alpha = list(string.ascii_lowercase)
alpha.extend(list(string.ascii_uppercase))

total_priority = 0


def find_common_item(compartment_one, compartment_two):
    for element in compartment_one:
        if element in compartment_two:
            return element


def get_item_priority(common):
    global alpha
    return alpha.index(common) + 1


def find_group_badge(elf1, elf2, elf3):
    for element in elf1:
        if element in elf2 and element in elf3:
            return element



# part 1
with open("data.txt") as file:
    for line in file:
        compartment_one, compartment_two = line[:len(line) // 2], line[len(line) // 2:]
        total_priority += get_item_priority(find_common_item(compartment_one, compartment_two))
print(f"Part 1: {total_priority}")
total_priority = 0

# part 2
with open("data.txt") as file:
    data = [line.strip() for line in file]

for i in range(0, len(data), 3):
    total_priority += get_item_priority(find_group_badge(data[i], data[i + 1], data[i + 2]))

print(f"Part 2: {total_priority}")
