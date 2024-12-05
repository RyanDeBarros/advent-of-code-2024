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


def less_than_two_errors(nums):
    if is_safe(nums):
        return True
    for i in range(len(nums)):
        try_nums = [num for num in nums]
        try_nums.pop(i)
        if is_safe(try_nums):
            return True
    return False


safe_counter = 0

with open("../inputs/Day2.txt", 'r') as file:
    for line in file:
        if less_than_two_errors([int(num) for num in line.split(' ')]):
            safe_counter += 1

print(safe_counter)
