from collections import deque

class BST(object):
    def __init__(self):
        self.height = None
        self.root = None
        self.size = 0

    def in_order_traversal(self):
        stack = deque()
        stack.appendleft(self.root)
        while stack:
            node = stack[0]
            if node.left and node.left.discovered == False:
                stack.appendleft(node.left)
                node.left.discovered = True
            else:
                print node.val
                stack.popleft()
                if node.right and node.right.discovered == False:
                    stack.appendleft(node.right)
                    node.right.discovered = True

    def build(self, nodes):
        for node in nodes:
            self.insert(node)

    def insert(self, node):
        if self.size == 0:
            self.root = node
            self.size += 1
        else:
            i = self.root
            while True:
                if i.val < node.val:
                    if i.right == None:
                        i.right = node
                        i.right.parent = i
                        i.subnodes += 1
                        break
                    else:
                        i = i.right
                if i.val > node.val:
                    if i.left == None:
                        i.left = node
                        i.left.parent = i
                        i.subnodes += 1
                        break
                    else:
                        i = i.left

