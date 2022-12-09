# 30373
# 25512
# 65332
# 33549
# 35390
import math

with open("data.txt") as file:
    grid = []
    for element in file.readlines():
        grid.append([int(x) for x in str(element.strip())])

total_visible = 0
max_view_score = 0


def is_edge(x_pos, y_pos):
    if x_pos == 0 or x_pos == len(grid[0]) - 1:
        return True
    elif y_pos == 0 or y_pos == len(grid) - 1:
        return True
    else:
        return False


def visible_left(x_pos, y_pos, height):
    global grid
    if x_pos == 0:
        return height > grid[x_pos][y_pos]
    if height <= grid[x_pos][y_pos]:
        return False
    return visible_left(x_pos - 1, y_pos, height)


def visible_right(x_pos, y_pos, height):
    global grid
    if x_pos == len(grid[0]) - 1:
        return height > grid[x_pos][y_pos]
    if height <= grid[x_pos][y_pos]:
        return False
    return visible_right(x_pos + 1, y_pos, height)


def visible_bottom(x_pos, y_pos, height):
    global grid
    if y_pos == len(grid) - 1:
        return height > grid[x_pos][y_pos]
    if height <= grid[x_pos][y_pos]:
        return False
    return visible_bottom(x_pos, y_pos + 1, height)


def visible_top(x_pos, y_pos, height):
    global grid
    if y_pos == 0:
        return height > grid[x_pos][y_pos]
    if height <= grid[x_pos][y_pos]:
        return False
    return visible_top(x_pos, y_pos - 1, height)


def is_visible(x_pos, y_pos, height):
    if visible_left(x_pos - 1, y_pos, height) \
            or visible_right(x_pos + 1, y_pos, height) \
            or visible_bottom(x_pos, y_pos + 1, height) \
            or visible_top(x_pos, y_pos - 1, height):
        return True


def look_left(x_pos, y_pos, height):
    if x_pos == 0 or grid[x_pos][y_pos] >= height:
        return 1
    return 1 + look_left(x_pos-1, y_pos, height)


def look_right(x_pos, y_pos, height):
    if x_pos == len(grid[0])-1 or grid[x_pos][y_pos] >= height:
        return 1
    return 1 + look_right(x_pos + 1, y_pos, height)


def look_down(x_pos, y_pos, height):
    if y_pos == len(grid) - 1 or grid[x_pos][y_pos] >= height:
        return 1
    return 1 + look_down(x_pos, y_pos + 1, height)


def look_up(x_pos, y_pos, height):
    if y_pos == 0  or grid[x_pos][y_pos] >= height:
        return 1
    return 1 + look_up(x_pos, y_pos - 1, height)


def get_scenic_score(x_pos, y_pos, height):
    global max_view_score, grid
    scores = [0, 0, 0, 0]
    scores[0] = look_left(x_pos - 1, y_pos, height)
    scores[1] = look_right(x_pos + 1, y_pos, height)
    scores[2] = look_down(x_pos, y_pos+1, height)
    scores[3] = look_up(x_pos, y_pos-1, height)
    if math.prod(scores) > max_view_score:
        max_view_score = math.prod(scores)


for x in range(len(grid)):
    for y in range(len(grid[0])):
        current = grid[x][y]
        if is_edge(x, y):
            total_visible += 1
            continue
        if is_visible(x, y, current):
            total_visible += 1
        get_scenic_score(x, y, current)

print(total_visible)
print(max_view_score)
