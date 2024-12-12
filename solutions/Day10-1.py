grid = []
trailheads = set()

y = 0
with open("../inputs/Day10.txt", 'r') as file:
    for line in file:
        row = [int(num) for num in line[:-1]]
        grid.append(row)
        for x in range(len(row)):
            if row[x] == 0:
                trailheads.add((x, y))
        y += 1


def fill_nines(position, i, group):
    global grid
    if position[0] < 0 or position[0] >= len(grid[0]) or position[1] < 0 or position[1] >= len(grid) or \
            grid[position[1]][position[0]] != i:
        pass
    elif i == 9:
        group.nines.add(position)
    elif position in group.travelled[i]:
        pass
    else:
        group.travelled[i].add(position)
        fill_nines((position[0] + 1, position[1]), i + 1, group)
        fill_nines((position[0] - 1, position[1]), i + 1, group)
        fill_nines((position[0], position[1] + 1), i + 1, group)
        fill_nines((position[0], position[1] - 1), i + 1, group)


class TrailGroup:
    def __init__(self):
        self.nines = set()
        self.travelled = {}
        for i in range(1, 9):
            self.travelled[i] = set()


total = 0
for trailhead in trailheads:
    group = TrailGroup()

    fill_nines((trailhead[0] + 1, trailhead[1]), 1, group)
    fill_nines((trailhead[0] - 1, trailhead[1]), 1, group)
    fill_nines((trailhead[0], trailhead[1] + 1), 1, group)
    fill_nines((trailhead[0], trailhead[1] - 1), 1, group)

    total += len(group.nines)

print(total)
