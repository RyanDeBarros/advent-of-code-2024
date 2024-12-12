with open("../inputs/Day11.txt", 'r') as file:
    lst = file.readline().split(' ')


def blink(nums):
    offset = 0
    for i in range(len(nums)):
        j = i + offset
        if nums[j] == '0':
            nums[j] = '1'
        elif len(nums[j]) & 1:
            nums[j] = str(2024 * int(nums[j]))
        else:
            left = nums[j][:len(nums[j])//2]
            right = str(int(nums[j][len(nums[j])//2:]))
            nums[j] = left
            nums.insert(j + 1, right)
            offset += 1


for _ in range(25):
    blink(lst)

print(len(lst))
