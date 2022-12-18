from string import ascii_lowercase
from heapq import heappop, heappush

with open("data.txt") as file:
    lines = file.read().strip().split()

grid = [list(line) for line in lines]
n = len(grid)
m = len(grid[0])
start = None
end = None

for i in range(n):
    for j in range(m):
        char = grid[i][j]
        if char == "S":
            start = i, j
        if char == "E":
            end = i, j


def get_height(c):
    if c in ascii_lowercase:
        return ascii_lowercase.index(c)
    if c == "S":
        return 0
    if c == "E":
        return 25


def neighbours(i, j):
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ii = i + di
        jj = j + dj

        if not (0 <= ii < n and 0 <= jj < m):
            continue

        # if get_height(grid[ii][jj]) <= get_height(grid[i][j]) + 1:
        #     yield ii, jj
        if get_height(grid[ii][jj]) >= get_height(grid[i][j]) -1:
            yield ii, jj


visited = [[False] * m for _ in range(n)]
heap = [(0, end[0], end[1])]

while True:
    steps, i, j = heappop(heap)

    if visited[i][j]:
        continue
    visited[i][j] = True

    # if (i, j) == end:
    #     print(steps)
    #     break
    if get_height(grid[i][j]) == 0:
        print(steps)
        break

    for ii, jj in neighbours(i, j):
        heappush(heap, (steps + 1, ii, jj))
