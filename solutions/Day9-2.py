with open("../inputs/Day9.txt", 'r') as file:
    disk_map = file.read()[:-1]

fs = []  # (num, val)

# load filesystem data structure
fid = 0
on_file_block = True
for digit in disk_map:
    if int(digit) != 0:
        if on_file_block:
            fs.append((int(digit), fid))
            fid += 1
        else:
            fs.append((int(digit), -1))
    on_file_block = not on_file_block

# re-arrange filesystem
i = len(fs) - 1
fid -= 1
while i >= 0 and fid >= 0:
    if fs[i][1] != fid:
        i -= 1
    else:
        moved = False
        for to in range(i):
            if fs[to][1] == -1 and fs[to][0] >= fs[i][0]:
                leftover = fs[to][0] - fs[i][0]
                fs[to] = fs[i]

                fs[i] = (fs[i][0], -1)
                while fs[i - 1][1] == -1:
                    fs[i - 1] = (fs[i - 1][0] + fs[i][0], -1)
                    del fs[i]
                    i -= 1
                while i < len(fs) - 1 and fs[i + 1][1] == -1:
                    fs[i] = (fs[i][0] + fs[i + 1][0], -1)
                    del fs[i + 1]

                if leftover == 0:
                    i -= 1
                else:
                    fs.insert(to + 1, (leftover, -1))
                fid -= 1
                moved = True
                break
        if not moved:
            i -= 1
            fid -= 1

# filesystem checksum
checksum = 0
i = 0
for block in fs:
    if block[1] != -1:
        trisum = block[0] * (block[0] + 2 * i - 1) // 2
        checksum += block[1] * trisum
    i += block[0]

print(checksum)
