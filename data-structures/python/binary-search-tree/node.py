class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.val = value
        self.discovered = False
        self.subnodes = 0

    def attach(self, node):
        if node.val > self.val:
            if self.right:
                raise TypeError("Attempted to attach larger node to node" +
                        " that already had a right child.")
            else:
                self.right = node
                self.right.parent = self
                self.subnodes += 1
        else:
            if self.left:
                raise TypeError("Attempted to attach larger node to node" +
                        " that already had a right child.")
            else:
                self.left = node
                self.left.parent = self
                self.subnodes += 1

