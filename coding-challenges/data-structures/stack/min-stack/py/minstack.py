from collections import deque
import sys

class MinStack:
    __slots__ = ['__stack', '__min_stack']

    def __init__(self):
        self.__stack = deque()
        self.__min_stack = deque()

    def push(self, val):
        self.__stack.append(val)

        if not self.__min_stack:
            self.__min_stack.append(val)
        elif self.__min_stack[-1] >= val:
            self.__min_stack.append(val)

    def pop(self):
        popped_val = self.__stack.pop()

        if self.__min_stack[-1] == popped_val:
            self.__min_stack.pop()

        return popped_val

    def min(self):
        return self.__min_stack[-1] if self.__min_stack else None

