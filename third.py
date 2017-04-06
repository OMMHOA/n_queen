from __future__ import print_function

start = -100
N = 10

def print_result(node):
    if (node.position != start):
        print_result(node.parent)
        print('%d,' % node.position, end='')    

class Node:

    def __init__(self, position, parent):
        self.good_child_index = 0
        self.position = position
        self.parent = parent

        if (parent != None):
            self.taboo = self.process_taboos(parent.taboo)
            self.level = parent.level + 1
        else:
            self.level = 0
            self.taboo = []

        if self.level >= N:
            print_result(self)
            print('')

        self.children = []
        for i in range(0, N):
            if self.taboo_not_contains(i) and abs(i - self.position) > 1:
                self.children.append(Node(i, self))

    def process_taboos(self, taboos):
        new_taboos = []
        new_taboos.append([self.position, 0])
        new_taboos.append([self.position, -1])
        new_taboos.append([self.position, 1])
        for i in range(len(taboos)):
            new_taboos.append(list(taboos[i]))
        for taboo in new_taboos:
            taboo[0] += taboo[1]
        return new_taboos

    def taboo_not_contains(self, position):
        for taboo in self.taboo:
            if (taboo[0] == position):
                return False
        return True

    def get_good_child(self):
        if self.good_child_index >= len(self.children):
            return None
        else:
            good_child = self.children[self.good_child_index]
            self.good_child_index += 1
            return good_child

N = int(raw_input('n: '))
Node(start, None)