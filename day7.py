import numpy as np
import copy

class Node(object):
    def __init__(self):
        self.data = None
        self.children = {}
        self.parent = None

    def add_child(self, name, obj):
        self.children[name] = obj
        if isinstance(obj, Node):
            obj.parent = self

    def getsize(self):
        val = 0
        val2 = 0
        for _,child in self.children.items():
            if isinstance(child, Node):
                sizes = child.getsize()
                val += sizes[0]
                val2 += sizes[1]
            else:
                val += child
        self.data = val
        if val < 100000:
            val2 += val
        return val, val2

    def find_min_dir(self, target):
        if self.data < target:
            return -1
        val = self.data
        for _,child in self.children.items():
            if isinstance(child, Node):
                val2 = child.find_min_dir(target)
                if val2 > 0:
                    val = min(val,val2)
        return val


    def find_del_dir(self):
        tot_size, _ = self.getsize()
        target = tot_size - (70000000 - 30000000)
        return self.find_min_dir(target)




if __name__ == "__main__":
    with open("day7.txt") as f:
        data = [[command.split('\n')[0], command.split('\n')[1:]] for command in f.read().split("\n$ ") if command]
    head_node = Node()
    curr_node = head_node
    for command in data[1:]:
        comm = command[0].split(' ')
        if (comm[0]) == 'cd':
            if comm[1] == '..':
                curr_node = curr_node.parent
            else:
                curr_node = curr_node.children[comm[1]]
        else:
            for item in command[1]:
                specs = item.split(' ')
                if specs[0] == "dir":
                    curr_node.add_child(specs[1], Node())
                else:
                    curr_node.add_child(specs[1], int(specs[0]))
    _, sol1 = head_node.getsize()
    sol2 = head_node.find_del_dir()

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
