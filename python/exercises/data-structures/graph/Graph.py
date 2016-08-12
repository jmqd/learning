import logging, pprint, Node
from queue import Queue
logging.basicConfig(level = logging.DEBUG)

class Graph:

    def __init__(self, data):
        logging.info('Calling Constructor for Graph.')
        self.graph = {}
        self.build(data)


    def build(self, data):
        logging.info('Calling Graph.build()')
        for key, values in data.items():
            self.graph[key] = Node.Node(key, set(values))
            logging.info('Building nodes for {}'.format(key))


    def search(self, start, end):
        self.reset_graph()
        self.graph[start].discover()
        queue = Queue()
        queue.put(self.graph[start])
        while not queue.empty():
            node = queue.get()
            for neighbor in node.get_neighbors():
                if not self.graph[neighbor].is_discovered():
                    self.graph[neighbor].discover()
                    if self.graph[neighbor].name == end:
                        return True
                    queue.put(self.graph[neighbor])
        return False


    def reset_graph(self):
        pass

    def show(self):
        logging.info('Showing graph...')
        pprint.pprint(self.graph)

