import Node, math, sys, queue, operator

class Heap:

    def __init__(self, **kwargs):

        data = kwargs.pop('data', ())
        self.type = kwargs.pop('type', 'max')
        self.tree = []
        self.queue = queue.Queue()
        if data:
            self.size = len(data)
            self.height = math.floor(math.log(self.size, 2))
            self.initialize_tree(data)
            self.build()


    def initialize_tree(self, data):
        for i in range(0, self.size):
            self.tree.append(Node.Node(value = data[i], heap = self, index = i))


    def build(self):
        for node in reversed(self.tree):
            if node.has_children():
                self.correct(node)


    def get_size(self):
        return self.size


    def insert(self, value):
        keywords = {
            'index': self.size,
            'value': value,
            'heap': self,
            }
        node = Node.Node(**keywords)
        self.tree.append(node)
        self.refresh()
        self.correct(node.parent())
        self.correct(node)
        return self


    def refresh(self):
        self.size = len(self.tree)
        self.height = math.floor(math.log(self.size, 2))


    def get_node(self, index):
        if index > self.size - 1:
            return False
        if index < 0:
            return False
        return self.tree[index]


    def resolve_queue(self):
        while not self.queue.empty():
            node = self.queue.get()
            self.correct(node)


    def swap(self, active, passive):
        i, j = active.get_index(), passive.get_index()
        self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
        active.set_index(j)
        passive.set_index(i)


    def find_max(self):
        return self.tree[0]


    def delete(self, node):
        index = node.get_index()
        self.swap(node, self.tree[self.size - 1])
        self.tree.pop()
        self.refresh()
        self.correct(self.tree[index])

    def correct(self, node):
        if node.largest_child() and node.largest_child().get_value() > node.get_value():
            node = self.maxify(node)
        while node.parent() and node.parent().get_value() < node.get_value():
            self.queue.put(node.parent())
            if node.get_sibling() and node.get_sibling().get_value() > node.get_value():
                node = node.get_sibling()
            self.swap(node.parent(), node)
            if node.is_root():
                break

    def maxify(self, node):
        possibles = [node, node.get_sibling(), node.parent()]
        possibles.sort(key = operator.attrgetter("value"), reverse = True)
        self.swap(possibles[0], possibles[len(possibles) - 1])
        return possibles[0]

    def draw(self):
        space_counter = 2**(self.height + 2) - 1
        string = ""
        node_i = 0
        for height in range(0, self.height + 1):
            space_between = space_counter * " "
            space_counter //= 2
            string += " " * space_counter
            for i in range(0, 2**height):
                if not self.get_node(node_i):
                    break
                string += str(self.get_node(node_i).get_value())
                string += space_between
                node_i += 1
            string += "\n"
        print(string)

