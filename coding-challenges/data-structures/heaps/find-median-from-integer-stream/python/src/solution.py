from typing import TypeVar
import heapq

Number = TypeVar('Number', float, int)

class Heap:
    def __init__(self) -> None:
        self._heap = []

    def __len__(self) -> int:
        return len(self._heap)

    def __bool__(self) -> bool:
        return len(self._heap) > 0


class MinHeap(Heap):
    def push(self, value: int) -> None:
        heapq.heappush(self._heap, value)

    def pop(self) -> int:
        return heapq.heappop(self._heap)

    def swap_top(self, value: int) -> int:
        root = self[0]
        self[0] = value
        heapq.heapify(self._heap)
        return root

    def __getitem__(self, i: int) -> int:
        return self._heap[i]


class MaxHeap(Heap):
    def push(self, value: int) -> None:
        heapq.heappush(self._heap, -value)

    def pop(self) -> int:
        return abs(heapq.heappop(self._heap))

    def swap_top(self, value: int) -> int:
        root = self[0]
        self[0] = value
        heapq._heapify_max(self._heap)
        return root

    def __getitem__(self, i: int) -> int:
        return abs(self._heap[i])


class MedianHeap:
    def __init__(self) -> None:
        self.lower = MaxHeap()
        self.upper = MinHeap()
        self.median = None

    def get_median(self) -> Number:
        if len(self) & 1:
            return self.median
        else:
            return (self.median + self.get_larger_heap()[0]) / 2

    def peek(self) -> int:
        return self.median

    def pop(self) -> int:
        median = self.median
        self.median = self.get_larger_heap().pop()
        return median

    def __len__(self):
        return sum([0 if self.median is None else 1,
                   len(self.lower),
                   len(self.upper)])

    @property
    def is_empty(self):
        return self.median is None and len(self.lower) == 0 and len(self.upper) == 0

    @property
    def is_unbalanced(self) -> bool:
        return abs(len(self.lower) - len(self.upper)) > 1

    def get_smaller_heap(self) -> Heap:
        return self.upper if len(self.lower) > len(self.upper) else self.lower

    def get_larger_heap(self) -> Heap:
        return self.lower if len(self.lower) > len(self.upper) else self.upper

    def push(self, value: int) -> None:
        if self.is_empty:
            self.median = value

        elif value > self.median:
            self.upper.push(value)

        elif value < self.median:
            self.lower.push(value)

        else:
            if len(self.upper) > len(self.lower):
                self.lower.push(value)
            else:
                self.upper.push(value)

        self.balance()

    def balance(self):
        while self.is_unbalanced:
            big_heap, small_heap = self.get_larger_heap(), self.get_smaller_heap()
            small_heap.push(self.median)
            self.median = big_heap.pop()

