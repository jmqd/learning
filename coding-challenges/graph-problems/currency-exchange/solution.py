'''
Given an input file like so:
---
USD,EUR,0.86
YEN,USD,0.0089
CNY,USD,0.14
EUR,GBP,0.88
GBP,USD,1.32
---

Answer a list of queries like so:
---
CNY,YEN
GBP,YEN
EUR,YEN
---

Returning the associated conversion rate.
'''
from collections import deque

def read_n_blocks(text, delimiter, n):
    split = text.split('\n')
    blocks = []
    i = 0
    while len(blocks) < n:
        while split[i] != delimiter:
            i += 1

        blocks.append([])
        i += 1

        while split[i] != delimiter:
            blocks[-1].append(split[i])
            i += 1

        i += 1

    return blocks

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

def main():
    exchange_rates, queries = (listify_csv(x) for x in read_n_blocks(__doc__, '---', 2))
    nodes = build_exchange_rate_graph(exchange_rates)
    answers = [bfs_exchange_rate(nodes, origin, target) for origin, target in queries]
    print(answers)

def build_exchange_rate_graph(exchange_rates):
    nodes = {}
    for src, target, rate in exchange_rates:
        rate = float(rate)

        if src not in nodes:
            nodes[src] = Node(src)

        node = nodes[src]

        if target not in nodes:
            nodes[target] = Node(target)

        target_node = nodes[target]

        node.neighbors[target] = (target_node, rate)
        target_node.neighbors[src] = (node, 1/rate)

    return nodes

def bfs_exchange_rate(nodes, origin, target):
    if not all(x in nodes for x in (origin, target)):
        print("One of {}, {} is not a graph in the node.".format(origin, target))
        return None

    queue = deque([[nodes[origin], 1]])
    seen = set()

    while queue:
        print(queue[-1])
        node, rate = queue.pop()

        if node.name in seen:
            continue
        else:
            seen.add(node.name)

        if target in node.neighbors:
            return rate * node.neighbors[target][1]
        else:
            for neighbor, neighbor_rate in node.neighbors.values():
                queue.appendleft([neighbor, neighbor_rate * rate])

def listify_csv(exchange_rates_csv):
    for line in exchange_rates_csv:
        yield line.split(',')

if __name__ == "__main__":
    main()
