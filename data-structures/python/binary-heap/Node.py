import logging
logging.basicConfig(level=logging.DEBUG)


class Node:

    def __init__(self, **kwargs):
        self.__index = kwargs.pop('index')
        self.__value = kwargs.pop('value')
        self.heap = kwargs.pop('heap')

    @property
    def index(self):
        return self.__index

    @property
    def value(self):
        return self.__value

    def parent(self):
        return self.heap.node((self.__index - 1) // 2)

    def left(self):
        return self.heap.node(2 * self.__index + 1)

    def right(self):
        return self.heap.node(2 * self.__index + 2)

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
        if self.__index == 0:
            logging.info('Node: Node is root.')
            return True

    def is_leaf(self):
        if len(self.children()) == 0:
            logging.info('Node: Node is leaf.')
            return True
        return False

    @index.setter
    def index(self, value):
        self.__index = value

    @value.setter
    def value(self, value):
        if value == self.value:
            self.__value = value
            return self
        if value > self.value:
            self.__value = value
            self.heap.queue.put(self)
            return self
        if value < self.value:
            self.__value = value
            self.heap.queue.put(self)
            return self

    def get_sibling(self):
        if self.is_left() and self.__index + 1 < self.heap.get_size():
            return self.heap.tree[self.__index + 1]
        if self.is_right():
            return self.heap.tree[self.__index - 1]
        else:
            return None


    def is_left(self):
        if self.is_root():
            return False
        if self.__index & 1 == 0:
            return False
        return True

    def is_right(self):
        if self.is_root():
            return False
        if not self.__index & 1 == 0:
            return False
        return True


    def largest_child(self):
        if self.is_leaf():
            logging.info('Node: Node is leaf -- node has no children.')
            return False
        if not self.left():
            if self.right():
                return self.right()
        if not self.right():
            if self.left():
                return self.left()
        if self.left().value > self.right().value:
            return self.left()
        return self.right()
