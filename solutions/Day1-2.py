dict1 = {}
dict2 = {}

with open("../inputs/Day1.txt", 'r') as file:
    for line in file:
        cols = line.split()
        key = int(cols[0].strip())
        if key in dict1.keys():
            dict1[key] += 1
        else:
            dict1[key] = 1
        key = int(cols[1].strip())
        if key in dict2.keys():
            dict2[key] += 1
        else:
            dict2[key] = 1

total = 0
for key, value in dict1.items():
    total += dict2.get(key, 0) * value * key

print(total)
