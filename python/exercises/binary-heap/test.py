import Heap, pprint

keywords = {
    'data': (5, 9, 20, 31, 14, 2, 5),
        }
heap = Heap.Heap(**keywords)
for node in heap.tree:
    print(node.__dict__)
