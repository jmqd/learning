class Node:
    def __init__(self, val: str, parent: 'Node') -> None:
        self.val = val
        self.parent = parent
        self.children = {}
        self.count = 1

    def has(self, val: str) -> bool:
        return val in self.children

    def get(self, val: str) -> bool:
        return self.children[val]

    def add(self, val: str) -> None:
        if self.has(val):
            self.children[val].count += 1
        else:
            self.children[val] = Node(val, self)

    def word(self):
        node = self
        word = ''
        while node.val:
            word += node.val
            node = node.parent
        return word[::-1]


class CountingPrefixTree:
    def __init__(self, target_count):
        self.tree = Node(None, None)
        self.target_count = target_count
        self.longest = ''

    def add(self, word: str) -> None:
        node = self.tree
        for i, char in enumerate(word):
            node.add(char)
            node = node.get(char)
            if node.count == target_count and len(self.longest) < (i + 1):
                self.longest = node.word()


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        tree = CountingPrefixTree(len(strs))
        for word in strs:
            tree.add(word)
        return tree.longest

