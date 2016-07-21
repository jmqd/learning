import Heap, pprint

keywords = {
    'data': (1, 2, 3),
        }
heap = Heap.Heap(**keywords)
for node in heap.tree:
    print(node.__dict__)
