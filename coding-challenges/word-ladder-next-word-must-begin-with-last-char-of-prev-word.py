from collections import defaultdict, deque

def make_graph(dictionary):
    adj_list = defaultdict(set)
    for word in dictionary:
        adj_list[word[0]].add(word[-1])
    return adj_list

def breadth_first_search(graph, origin, target):
    q = deque()
    q.appendleft([origin[-1], 1])
    seen = set()

    while q:
        node, level = q.pop()
        if node in seen:
            continue
        else:
            seen.add(node)

        if node == target[0]:
            return level

        q.extendleft([[c, level + 1] for c in graph[node]])

def main():
    with open('/usr/share/dict/words', 'r') as f:
        data = [l.strip().lower() for l in f]

    graph = make_graph(data)
    ans = breadth_first_search(graph, "fizz", "queue")
    print(ans)

if __name__ == "__main__":
    main()
