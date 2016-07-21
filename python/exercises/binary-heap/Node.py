class Node:

    def __init__(self, **kwargs):
        self.index = kwargs.pop('index')
        self.value = kwargs.pop('value')
        self.heap = kwargs.pop('heap')

    def get_index(self):
        return self.index

    def get_value(self):
        return self.value

    def parent(self):
        return self.heap.get_node((self.index - 1) // 2)

    def left(self):
        return self.heap.get_node(2 * self.index + 1)

    def right(self):
        return self.heap.get_node(2 * self.index + 2)

    def set_index(self, index):
        self.index = index

    def set_value(self, value):
        self.value = value

    def has_children(self):
        if self.left() or self.right():
            return True
        return False

    def children(self):
        children = []
        if self.left():
            children.append(self.left())
        if self.right():
            children.append(self.right())
        return children

    def is_root(self):
        if self.index == 0:
            return True
