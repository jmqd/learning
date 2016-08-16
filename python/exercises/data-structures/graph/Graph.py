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
        logging.info('Searching for path from {} to {}'.format(start, end))
        self.reset_graph()
        self.graph[start].discover()
        queue = Queue()
        root = self.graph[start]
        root.set_distance(0)
        if start == end:
            # make sure to create method on node to get path
            # and implement it here.
            return root
        root = self.graph[start]
        root.set_distance(0)
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            for neighbor in node.get_neighbors():
                if not self.graph[neighbor].is_discovered():
                    logging.info('discovered {}'.format(neighbor))
                    self.graph[neighbor].discover().set_distance(node.distance + 1)
                    self.graph[neighbor].set_parent(node)
                    if self.graph[neighbor].name == end:
                        return (True,
                                self.graph[neighbor].distance,
                                self._path_to(self.graph[start],
                                             self.graph[neighbor]))
                    queue.put(self.graph[neighbor])
        return (False, None)


    def _path_to(self, start, node):
        path = []
        path.append(node.name)
        logging.info('Added {} to path'.format(node.name))
        parent = node.get_parent()
        while parent != start:
            logging.info('Added {} to path'.format(parent.name))
            path.append(parent.name)
            parent = parent.get_parent()
        path.append(start.name)
        return list(reversed(path))




    def reset_graph(self):
        pass

    def show(self):
        logging.info('Showing graph...')
        pprint.pprint(self.graph)

