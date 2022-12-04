data = []
with open("data.txt") as file:
    for line in file:
        data.append(line.strip().split(','))

total1 = 0
total2 = 0


def pair_fully_contains(pair1, pair2):
    lower1 = int(pair1[0])
    lower2 = int(pair2[0])
    higher1 = int(pair1[1])
    higher2 = int(pair2[1])
    return lower1 >= lower2 and higher1 <= higher2


def pair_overlaps(pair1, pair2):
    lower1 = int(pair1[0])
    lower2 = int(pair2[0])
    higher1 = int(pair1[1])
    higher2 = int(pair2[1])
    set1 = [item for item in range(lower1, higher1+1)]
    set2 = [item for item in range(lower2, higher2+1)]
    intersection = set(set1).intersection(set2)
    return len(intersection) != 0


for element in data:
    current = [element[0].split('-'), element[1].split('-')]
    if pair_fully_contains(current[0], current[1]) or pair_fully_contains(current[1], current[0]):
        total1 += 1
    if pair_overlaps(current[0], current[1]) or pair_overlaps(current[1], current[0]):
        total2 += 1

print(f"Part 1: {total1}")
print(f"Part 2: {total2}")
