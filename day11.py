import numpy as np
import copy


class Monkey:
    def __init__(self, raw):
        data = raw.split('\n')
        self.id = data[0].split(' ')[1]
        self.items = [int(x) for x in data[1].split(': ')[1].strip().split(',')]
        self.operation = data[2].strip().split(' ')[4]
        self.constant = data[2].strip().split(' ')[5]
        self.divisor = int(data[3].split(' ')[-1])
        self.destTrue = int(data[4].split(' ')[-1])
        self.destFalse = int(data[5].split(' ')[-1])

    def inspect(self, part2=0):
        output = {}
        output[self.destTrue] = []
        output[self.destFalse] = []
        for item in self.items:
            if self.constant == "old":
                constant = item
            else:
                constant = int(self.constant)
            if self.operation == "*":
                val = item * constant
            else:
                val = item + constant
            if part2:
                val = val % part2
            else:
                val = val//3
            if val % self.divisor:
                output[self.destFalse].append(val)  
            else:
                output[self.destTrue].append(val)
        self.items = []
        return output

    def addItems(self,items):
        for item in items:
            self.items.append(item)

def do_part(monkeys, part2=False):
    data = copy.deepcopy(monkeys)
    inspections = [0]*len(data)
    modulo = 0
    if part2:
        numIter = 10000
        modulo = int(np.prod([x.divisor for x in monkeys]))
    else:
        numIter = 20
    print(modulo)
    for i in range(numIter):
        for j, monkey in enumerate(data):
            throws = monkey.inspect(modulo)
            for key in throws:
                data[key].addItems(throws[key])
                inspections[j] += len(throws[key])
    inspections = sorted(inspections,reverse=True)
    return inspections[0]*inspections[1]


if __name__ == "__main__":
    with open("day11.txt") as f:
        data = [x for x in f.read().split("\n\n") if x]
    monkeys = []
    for monkey in data:
        monkeys.append(Monkey(monkey))

    sol1 = do_part(monkeys)
    sol2 = do_part(monkeys,True)

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
