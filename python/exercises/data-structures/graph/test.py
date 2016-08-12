from Graph import *

dictionary = {
    'cat': ['rat', 'bat', 'mat', 'pat', 'car'],
    'rat': ['cat', 'bat', 'mat', 'pat'],
    'car': ['cat'],
    'bat': ['cat', 'rat', 'mat', 'pat'],
    'pat': ['cat', 'rat', 'mat', 'bat'],
    'mat': ['cat', 'rat', 'bat', 'pat'],
}

graph = Graph(dictionary)
for node in graph.graph.values():
    print(node.get_neighbors())
graph.show()
print(graph.search('cat', 'pat'))
