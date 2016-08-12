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
        logging.info('Searching for path to {} from {}'.format(end, start))
        self.reset_graph()
        self.graph[start].discover()
        queue = Queue()
        distance = 0
        if start == end:
            self.graph[start].set_distance(distance)
            path = start
            return (True, distance, path)
        queue.put(self.graph[start])
        while not queue.empty():
            node = queue.get()
            distance += 1
            for neighbor in node.get_neighbors():
                if not self.graph[neighbor].is_discovered():
                    self.graph[neighbor].discover().set_distance(distance)
                    self.graph[neighbor].set_parent(node)
                    if self.graph[neighbor].name == end:
                        return (True,
                                distance,
                                self.path_to(self.graph[start],
                                             self.graph[neighbor]))
                    queue.put(self.graph[neighbor])
        return (False, None)


    def path_to(self, start, node):
        path = []
        path.append(node.name)
        parent = node.get_parent()
        while node.get_parent() != start:
            path.append(parent.name)
            parent = self.graph[node.parent()]
        path.append(start.name)
        return list(reversed(path))




    def reset_graph(self):
        pass

    def show(self):
        logging.info('Showing graph...')
        pprint.pprint(self.graph)

