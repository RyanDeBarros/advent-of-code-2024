import re

with open("../inputs/Day3.txt", 'r') as file:
    content = file.read()

matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", content)
total = 0
do = True
for match in matches:
    if match[2] == "do()":
        do = True
    elif match[3] == "don't()":
        do = False
    elif do:
        total += int(match[0]) * int(match[1])

print(total)
