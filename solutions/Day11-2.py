def add_to_dict(d, n, c):
    if n in d:
        d[n] += c
    else:
        d[n] = c


cache = {}
with open("../inputs/Day11.txt", 'r') as file:
    lst = file.readline().split(' ')
    for num in lst:
        add_to_dict(cache, num, 1)


def blink(cache):
    new_cache = {}
    for num, count in cache.items():
        if num == '0':
            add_to_dict(new_cache, '1', count)
        elif len(num) & 1:
            new_num = str(2024 * int(num))
            add_to_dict(new_cache, new_num, count)
        else:
            left = num[:len(num)//2]
            right = str(int(num[len(num)//2:]))
            add_to_dict(new_cache, left, count)
            add_to_dict(new_cache, right, count)
    return new_cache


for _ in range(75):
    cache = blink(cache)

total = 0
for k, v in cache.items():
    total += v

print(total)
