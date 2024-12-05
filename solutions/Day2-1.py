def is_safe(nums):
    increasing = None
    prev = None
    for num in nums:
        if prev is None:
            prev = num
            continue
        if num == prev or abs(num - prev) > 3:
            return False
        if increasing is None:
            increasing = num > prev
            prev = num
            continue
        if (increasing and num < prev) or (not increasing and num > prev):
            return False
        prev = num
    return True


safe_counter = 0

with open("../inputs/Day2.txt", 'r') as file:
    for line in file:
        if is_safe([int(num) for num in line.split(' ')]):
            safe_counter += 1

print(safe_counter)
