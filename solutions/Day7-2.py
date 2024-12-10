from enum import Enum


class Op(Enum):
    ADD = 0
    MULT = 1
    CONCAT = 2


class Equation:
    def __init__(self, line):
        arr = line.split(' ')
        self.result = int(arr[0][:-1])
        self.nums = [int(num) for num in arr[1:]]

    def valid(self):
        if self.valid_recur(0, Op.ADD, 0):
            return True
        elif self.valid_recur(0, Op.MULT, 0):
            return True
        elif self.valid_recur(0, Op.CONCAT, 0):
            return True
        else:
            return False

    def valid_recur(self, i, op, running_res):
        if i == len(self.nums):
            return running_res == self.result
        match op:
            case Op.ADD:
                running_res += self.nums[i]
            case Op.MULT:
                running_res *= self.nums[i]
            case Op.CONCAT:
                running_res = int(str(running_res) + str(self.nums[i]))
        if running_res > self.result:
            return False
        if self.valid_recur(i + 1, Op.ADD, running_res):
            return True
        elif self.valid_recur(i + 1, Op.MULT, running_res):
            return True
        elif self.valid_recur(i + 1, Op.CONCAT, running_res):
            return True
        else:
            return False


equations = []

with open("../inputs/Day7.txt", 'r') as file:
    for fline in file:
        equations.append(Equation(fline))

total = 0
for eqn in equations:
    if eqn.valid():
        total += eqn.result

print(total)
