import Node, math, logging

logging.basicConfig(level=logging.DEBUG)

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


    def initialize_tree(self, data):
        for i in range(0, self.size):
            self.tree.append(Node.Node(value = data[i], heap = self, index = i))


    def build(self):
        for i in range (self.size -1, -1, -1):
            if self.tree[i].has_children():
                self.heapify(self.tree[i])


    def get_size(self):
        return self.size


    def insert(self, value):
        keywords = {
            'index': self.size,
            'value': value,
            'heap': self,
            }
        node = Node.Node(**keywords)
        logging.info('inserting node (index: {}, value: {})'.format(node.get_index(),
                                                                    node.get_value()))
        self.tree.append(node)
        self.refresh()
        self.heapify(node.parent(), going_up = True)


    def refresh(self):
        self.size = len(self.tree)
        self.height = math.floor(math.log(self.size, 2))
        logging.info('Refreshed Heap: size: {}, height: {}'.format(self.size, self.height))


    def get_node(self, index):
        if index > self.size - 1:
            return False
        if index < 0:
            return False
        return self.tree[index]


    def swap(self, active, passive):
        i, j = active.get_index(), passive.get_index()
        logging.info('swapping ({}, {}) with ({}, {})'.format(i,
                                                              active.get_value(),
                                                              j,
                                                              passive.get_value()))
        self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
        active.set_index(j)
        passive.set_index(i)


    def find_max(self):
        return self.tree[0]


    def delete(self, node):
        logging.info('deleting node ({}, {})'.format(node.get_index(), node.get_value()))
        index = node.get_index()
        self.swap(node, self.tree[self.size - 1])
        self.tree.pop()
        self.refresh()
        self.heapify(self.tree[index])

    def heapify(self, node, going_up = False):
        if not node:
            logging.info('Node was false; passing on heapify.')
            return
        logging.info('heap-checking: (i: {}, v: {})'.format(node.get_index(), node.get_value()))
        largest = node.largest_child()
        if not largest:
            return
        if largest.get_value() > node.get_value():
            self.swap(node, largest)
            if going_up:
                if node.is_root():
                    logging.info('Node is root; heapify is complete.')
                    return
                return self.heapify(largest.parent(), going_up = True)
            return self.heapify(node)

    def draw(self):
        logging.info('drawing heap tree...')
        space_counter = 2**(self.height + 2) - 1
        string = ""
        node_i = 0
        for height in range(0, self.height + 1):
            space_between = space_counter * "-"
            space_counter //= 2
            string += " " * space_counter
            for i in range(0, 2**height):
                if not self.get_node(node_i):
                    break
                string += str(self.get_node(node_i).get_value())
                if node_i != 0 and i + 1 != 2**height:
                    string += space_between
                node_i += 1
            string += "\n"
        print(string)

