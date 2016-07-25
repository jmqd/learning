import Heap, pprint, random

keywords = {
    'data': (1, 5, 9, 6, 7, 4, 3),
        }
heap = Heap.Heap(**keywords)
heap.insert(55)
heap.draw()
