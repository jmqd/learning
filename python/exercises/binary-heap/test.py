import Heap, pprint, random

keywords = {
    'data': (5, 9, 20, 31, 14, 2, 5),
        }
heap = Heap.Heap(**keywords)
heap.insert(55)
heap.insert(54)
heap.insert(53)
heap.insert(53)
heap.insert(52)
heap.insert(100)
heap.delete(heap.tree[0])
heap.insert(5)
heap.insert(101)
for i in range(0, 40):
    heap.insert(random.randint(1, 99))
for node in heap.tree:
    pprint.pprint(node.__dict__)
heap.draw()
