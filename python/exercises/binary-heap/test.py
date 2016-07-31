import Heap, pprint, random

keywords = {
    'data': (1, 5, 22, 33, 14, 9, 6, 7, 4, 3),
        }
heap = Heap.Heap(**keywords)
heap.insert(55)
heap.insert(100)
heap.insert(22)
heap.draw()
