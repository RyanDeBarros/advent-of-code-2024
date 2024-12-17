class EquivalenceClasses:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x

    def get_sets(self):
        sets = {}
        for x in self.parent:
            root = self.find(x)
            if root not in sets:
                sets[root] = set()
            sets[root].add(x)
        return list(sets.values())


groupID = 0
groups = {}
joinedIDs = []

with open("../inputs/Day12.txt", 'r') as file:
    y = 0
    for line in file:
        for x in range(len(line) - 1):
            char = line[x]
            if y > 0 and groups[(x, y - 1)][0] == char:
                groups[(x, y)] = groups[(x, y - 1)]
                if x > 0 and groups[(x - 1, y)][0] == char:
                    joinedIDs.append((groups[x, y - 1][1], groups[x - 1, y][1]))
            elif x > 0 and groups[(x - 1, y)][0] == char:
                groups[(x, y)] = groups[(x - 1, y)]
            else:
                groups[(x, y)] = (char, groupID)
                groupID += 1
        y += 1

regions = {}
for k, v in groups.items():
    if v[1] < len(regions):
        regions[v[1]].add(k)
    else:
        regions[v[1]] = set()
        regions[v[1]].add(k)

ec = EquivalenceClasses()
for a, b in joinedIDs:
    ec.add(a)
    ec.add(b)
    ec.union(a, b)
joinedIDs = ec.get_sets()

for jid_set in joinedIDs:
    _to = min(jid_set)
    for _from in jid_set:
        if _from != _to:
            for v in regions[_from]:
                regions[_to].add(v)
            del regions[_from]

total = 0
for region in regions.values():
    sides = 0
    for plot in region:
        if (plot[0] - 1, plot[1]) not in region:
            if (plot[0], plot[1] - 1) not in region or (plot[0] - 1, plot[1] - 1) in region:
                sides += 1
        if (plot[0] + 1, plot[1]) not in region:
            if (plot[0], plot[1] - 1) not in region or (plot[0] + 1, plot[1] - 1) in region:
                sides += 1
        if (plot[0], plot[1] - 1) not in region:
            if (plot[0] - 1, plot[1]) not in region or (plot[0] - 1, plot[1] - 1) in region:
                sides += 1
        if (plot[0], plot[1] + 1) not in region:
            if (plot[0] - 1, plot[1]) not in region or (plot[0] - 1, plot[1] + 1) in region:
                sides += 1
    total += sides * len(region)
    print(region, sides * len(region))

print(total)
