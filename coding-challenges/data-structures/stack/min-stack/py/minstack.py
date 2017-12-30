from collections import deque
from typing import Iterable
from typing import TypeVar
import sys

Comparable = TypeVar('Comparable')

class MinStack:
    __slots__ = ['__stack', '__min_stack']

    def __init__(self, items: Iterable[Comparable]=None) -> None:
        self.__stack = deque()
        self.__min_stack = deque()

        if items is None:
            items = []

        for i in items:
            self.push(i)

    def push(self, val: int) -> None:
        self.__stack.append(val)

        if not self.__min_stack:
            self.__min_stack.append(val)
        elif self.__min_stack[-1] >= val:
            self.__min_stack.append(val)

    def pop(self) -> Comparable:
        popped_val = self.__stack.pop()

        if self.__min_stack[-1] == popped_val:
            self.__min_stack.pop()

        return popped_val

    def min(self) -> Comparable:
        return self.__min_stack[-1] if self.__min_stack else None

