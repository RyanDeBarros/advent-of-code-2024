rules = set()
with open("../inputs/Day5-1.txt", 'r') as file:
    for line in file:
        rules.add((int(line[0:2]), int(line[3:5])))


def satisfies_rules(num1, num2):
    global rules
    return (num1, num2) in rules or (num2, num1) not in rules


def valid_update(nums):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if not satisfies_rules(nums[i], nums[j]):
                return False
    return True


total = 0
with open("../inputs/Day5-2.txt", 'r') as file:
    for line in file:
        update = [int(num.strip()) for num in line.split(',')]
        if valid_update(update):
            total += int(update[len(update) // 2])

print(total)
