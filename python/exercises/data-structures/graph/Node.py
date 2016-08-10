class Node:

    def __init__(self, graph, value):
        self.value = value
        self.is_discovered = False
        self.distance = None
        self.graph = graph

    def neighbors(self):
        return self.graph[self.value]

    def has(self, neighbor):
        if neighbor in self.neighbors():
            return True
        return False

