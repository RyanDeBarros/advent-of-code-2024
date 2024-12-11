class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int):
        return Position(self.x * other, self.y * other)

    def __rmul__(self, other: int):
        return Position(self.x * other, self.y * other)

    def __hash__(self):
        return hash(self.x) ^ (hash(self.y) << 1)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def in_bounds(self, w, h):
        return 0 <= self.x < w and 0 <= self.y < h


grid = []
antenna_groups = {}
unique_antinodes = set()

y = 0
with open("../inputs/Day8.txt", 'r') as file:
    for line in file:
        row = line.strip()
        grid.append(row)
        for x in range(len(row)):
            char = row[x]
            if char != '.':
                if char in antenna_groups:
                    antenna_groups[char].append(Position(x, y))
                else:
                    antenna_groups[char] = [Position(x, y)]
        y += 1

for _, locations in antenna_groups.items():
    for i in range(len(locations) - 1):
        for j in range(i + 1, len(locations)):
            antinode = 2 * locations[i] - locations[j]
            if antinode.in_bounds(len(grid[0]), len(grid)):
                unique_antinodes.add(antinode)
            antinode = 2 * locations[j] - locations[i]
            if antinode.in_bounds(len(grid[0]), len(grid)):
                unique_antinodes.add(antinode)

print(len(unique_antinodes))
