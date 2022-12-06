with open("data.txt") as file:
    signal = file.readline()


def find_marker(sig, n):
    for i in range(0, len(sig)):
        if len(set(sig[i:i + n])) == n:  # convert current window to set, if == n, must be unique values for given size.
            return i + n


print(f"Part 1: {find_marker(signal, 4)}")
print(f"Part 2: {find_marker(signal, 14)}")
