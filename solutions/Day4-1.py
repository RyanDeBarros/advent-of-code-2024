grid = []
with open("../inputs/Day4.txt", 'r') as file:
    for line in file:
        grid.append(line)

count = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] != 'X':
            continue
        if col < len(grid[row]) - 3:
            # right
            if grid[row][col+1:col+4] == 'MAS':
                count += 1
            # up-right
            if row >= 3 and grid[row-1][col+1] == 'M' and grid[row-2][col+2] == 'A' and grid[row-3][col+3] == 'S':
                count += 1
            # down-right
            if row < len(grid) - 3 and grid[row+1][col+1] == 'M' and grid[row+2][col+2] == 'A' and grid[row+3][col+3] == 'S':
                count += 1
        if col >= 3:
            # left
            if grid[row][col-3:col] == 'SAM':
                count += 1
            # up-left
            if row >= 3 and grid[row-1][col-1] == 'M' and grid[row-2][col-2] == 'A' and grid[row-3][col-3] == 'S':
                count += 1
            # down-left
            if row < len(grid) - 3 and grid[row+1][col-1] == 'M' and grid[row+2][col-2] == 'A' and grid[row+3][col-3] == 'S':
                count += 1
        # up
        if row >= 3 and grid[row-1][col] == 'M' and grid[row-2][col] == 'A' and grid[row-3][col] == 'S':
            count += 1
        # down
        if row < len(grid) - 3 and grid[row+1][col] == 'M' and grid[row+2][col] == 'A' and grid[row+3][col] == 'S':
            count += 1

print(count)
