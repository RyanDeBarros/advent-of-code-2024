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
i = 0
while i < len(fs):
    while fs[len(fs) - 1][1] == -1:
        del fs[len(fs) - 1]
    last = len(fs) - 1
    if fs[i][0] == 0:
        del fs[i]
    elif fs[i][1] != -1:
        i += 1
    elif fs[i][0] == fs[last][0]:
        fs[i] = (fs[i][0], fs[last][1])
        i += 1
        del fs[last]
    elif fs[i][0] > fs[last][0]:
        leftover = fs[i][0] - fs[last][0]
        fs[i] = (fs[last][0], fs[last][1])
        i += 1
        fs.insert(i, (leftover, -1))
        del fs[last + 1]
    else:
        leftover = fs[last][0] - fs[i][0]
        fs[i] = (fs[i][0], fs[last][1])
        i += 1
        fs[last] = (leftover, fs[last][1])

# filesystem checksum
checksum = 0
i = 0
for block in fs:
    trisum = block[0] * (block[0] + 2 * i - 1) // 2
    checksum += block[1] * trisum
    i += block[0]

print(checksum)
