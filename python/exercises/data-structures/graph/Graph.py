import numpy as np, logging
from Node import *

logging.basicConfig(level = logging.DEBUG)

class Graph:

    def __init__(self, data):
        logging.info('Calling Constructor for Graph.')
        self.graph = {}
        self.build(data)


    def build(self, data):
        logging.info('Calling Graph.build()')
        for key, values in data.items():
            logging.info('Building nodes for {}'.format(key))
            self.graph[key] = []
            for value in values:
                logging.info('Added {} as neighbor to {}'.format(value, key))
                self.graph[key].append(Node(self.graph, value))

    def show(self):
        print(self.graph)

