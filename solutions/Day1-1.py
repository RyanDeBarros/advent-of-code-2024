from bisect import insort

list1 = []
list2 = []

with open("../inputs/Day1.txt", 'r') as file:
    for line in file:
        cols = line.split()
        insort(list1, int(cols[0].strip()))
        insort(list2, int(cols[1].strip()))

difference = 0
for i in range(len(list1)):
    difference += abs(list1[i] - list2[i])

print(difference)
