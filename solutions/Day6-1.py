grid = []

position = [0, 0]
direction = 0  # 0: up, 1: right, 2: down, 3: left

with open("../inputs/Day6.txt", 'r') as file:
    for line in file:
        row = list(line)
        try:
            x = row.index('^')
            position[0] = x
            position[1] = len(grid)
            row[x] = '.'
        except ValueError:
            pass
        grid.append(row)


def next_position():
    global direction, position
    if direction == 0:
        delta = [0, -1]
    elif direction == 1:
        delta = [1, 0]
    elif direction == 2:
        delta = [0, 1]
    else:
        delta = [-1, 0]
    return [position[0] + delta[0], position[1] + delta[1]]


travelled = set()

while True:
    next_pos = next_position()
    if next_pos[0] < 0 or next_pos[0] >= len(grid[0]) or next_pos[1] < 0 or next_pos[1] >= len(grid):
        break
    if grid[next_pos[1]][next_pos[0]] == '#':
        direction = (direction + 1) % 4
        continue
    position = next_pos
    travelled.add(tuple(position))

print(len(travelled))
