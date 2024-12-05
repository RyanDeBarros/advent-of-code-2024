import re

with open("../inputs/Day3.txt", 'r') as file:
    content = file.read()

matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", content)
total = 0
for match in matches:
    total += int(match[0]) * int(match[1])

print(total)
