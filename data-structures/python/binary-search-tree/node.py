class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.val = value
        self.discovered = False
        self.subnodes = 0
