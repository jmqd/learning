import Node, math, sys

class Heap:

    def __init__(self, **kwargs):

        data = kwargs.pop('data', ())
        self.type = kwargs.pop('type', 'max')
        self.tree = []
        if data:
            self.size = len(data)
            self.height = math.floor(math.log(self.size, 2))
            self.initialize_tree(data)
            self.build()
        self.last = self.tree[self.size - 1]


    def initialize_tree(self, data):
        for i in range(0, self.size):
            self.tree.append(Node.Node(value = data[i], heap = self, index = i))


    def build(self):
        for node in reversed(self.tree):
            if node.has_children():
                for child in node.children():
                    if not self.verify(child):
                        self.correct(child)


    def insert(self, value):
        keywords = {
            'index': self.size,
            'value': value,
            'heap': self,
            }
        node = Node.Node(**keywords)
        self.tree.append(node)
        if not self.verify(node):
            self.correct(node)
        self.size += 1
        return self


    def get_node(self, index):
        if index > self.size - 1:
            return False
        return self.tree[index]

    def verify(self, node):
        if node.parent().get_value() >= node.get_value():
            return True
        return False


    def correct(self, node):
        while node.parent().get_value() < node.get_value():
            self.swap(node.parent(), node)
            if node.is_root():
                break


    def swap(self, a, b):
        i, j = a.get_index(), b.get_index()
        self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
        a.set_index(j)
        b.set_index(i)


    def delete(self, node):
        self.swap(node, self.last)
        self.tree.pop()
        self.size -= 1
