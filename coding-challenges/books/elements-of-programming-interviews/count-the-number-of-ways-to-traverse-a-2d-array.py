import time

def find_neighbors(y, x, max_y, max_x):
    neighbors = []
    if y + 1 <= max_y:
        neighbors.append(tuple([y + 1, x]))
    if x + 1 <= max_x:
        neighbors.append(tuple([y, x + 1]))
    return tuple(neighbors)

def count_ways(y, x, target, cache):
    if (y, x) == target:
        return 1

    cache[(y, x)] = 0
    neighbors = find_neighbors(y, x, *target)
    for neighbor in neighbors:
        if neighbor not in cache:
            y_n, x_n = neighbor
            cache[neighbor] = count_ways(y_n, x_n, target, cache)
        cache[(y, x)] += cache[neighbor]
    return cache[(y, x)]

def solve(target):
    cache = {}
    answer = count_ways(0, 0, target, cache)
    print(target, "has", answer, "paths")

def test():
    for n in range(0, 20):
        start = time.time()
        solve((n, n))
        end = time.time()
        print((n, n), "took", end - start)

if __name__ == "__main__":
    test()
