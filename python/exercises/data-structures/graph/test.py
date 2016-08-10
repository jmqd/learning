from Graph import *

dictionary = {
    'cat': ['rat', 'bat', 'mat', 'pat', 'car'],
    'rat': ['cat', 'bat', 'mat', 'pat'],
    'car': ['far', 'bar', 'cat'],
    'bat': ['cat', 'rat', 'mat', 'pat'],
    'pat': ['cat', 'rat', 'mat', 'bat'],
    'mat': ['cat', 'rat', 'bat', 'pat'],
}

graph = Graph(dictionary)
graph.show()
