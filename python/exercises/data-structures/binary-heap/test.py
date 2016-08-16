import Heap, pprint, random

keywords = {
    'data': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        }
heap = Heap.Heap(**keywords)
heap.insert(44)
heap.insert(44)
heap.insert(32)
heap.insert(144)
heap.insert(11)
heap.insert(23)
heap.insert(144)
heap.draw()
