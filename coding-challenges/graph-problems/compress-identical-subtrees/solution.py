import hashlib
import sys

class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children if children else []

    def __str__(self):
        return "Node:{}".format(self.val)

def compress_identical_subtrees(root_node):
    print("Original size of tree is", dfs_calculate_size(root_node, set()))
    seen_subtrees = dict()
    serialized_dag = dfs(root_node, seen_subtrees)
    print("Subtrees that were recorded are", seen_subtrees)
    print("Serialized DAG (previously tree) is", serialized_dag)
    print("Size after compressing identical subtrees is", dfs_calculate_size(root_node, set()))

def dfs(node, seen_subtrees):
    print(node.val, id(node))
    if not node.children:
        return str(node.val)

    serialized_subtree = ''
    for child_index, child in enumerate(node.children):
        serialized_child = dfs(child, seen_subtrees)
        serialized_subtree += serialized_child

        if child.children:
            if serialized_child in seen_subtrees:
                node.children[child_index] = seen_subtrees[serialized_child]
            else:
                seen_subtrees[serialized_child] = child

    return serialized_subtree + str(node.val)

def run_example_case():
    root = create_example_tree()
    compress_identical_subtrees(root)

def create_example_tree():
    root = Node(1)
    left, right = Node(2), Node(2)
    root.children.extend((left, right))
    left_left, left_right = Node(4), Node(5)
    left.children.extend((left_left, left_right))
    right_left, right_right = Node(4), Node(5)
    right.children.extend((right_left, right_right))
    return root

def dfs_calculate_size(node, seen):
    if node in seen:
        return 0
    else:
        seen.add(node)

    size = sys.getsizeof(node)
    if node.children:
        for n in node.children:
            size += dfs_calculate_size(n, seen)
    return size

if __name__ == "__main__":
    run_example_case()
