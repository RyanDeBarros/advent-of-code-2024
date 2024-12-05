grid = []
with open("../inputs/Day4.txt", 'r') as file:
    for line in file:
        grid.append(line)

count = 0
for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[row]) - 1):
        if grid[row][col] != 'A':
            continue
        if (grid[row-1][col-1] == 'M' and grid[row+1][col+1] == 'S') or (grid[row-1][col-1] == 'S' and grid[row+1][col+1] == 'M'):
            if (grid[row-1][col+1] == 'M' and grid[row+1][col-1] == 'S') or (grid[row-1][col+1] == 'S' and grid[row+1][col-1] == 'M'):
                count += 1

print(count)
