import random
from node import Node
from tree import BST

def main():
    randints = [random.randint(0, 1000) for _ in range(50)]
    intkeys = set(randints)
    nodes = []
    for key in intkeys:
        nodes.append(Node(key))

    bst = BST()
    bst.build(nodes)
    bst.in_order_traversal()

if __name__ == '__main__':
    main()

