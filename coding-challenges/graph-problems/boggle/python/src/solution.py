from typing import List, Set, Callable, Tuple
from collections import deque

def sum_pairwise(origin: Tuple[int, int], delta: Tuple[int, int]) -> Tuple[int, int]:
    return tuple(map(sum, zip(origin, delta)))

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)
UP_LEFT = sum_pairwise(UP, LEFT)
UP_RIGHT = sum_pairwise(UP, RIGHT)
DOWN_LEFT = sum_pairwise(DOWN, LEFT)
DOWN_RIGHT = sum_pairwise(DOWN, RIGHT)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT]

CharGrid = List[List[str]]

def solve(character_grid: CharGrid, is_word: Callable) -> Set[str]:
    validate_grid_not_empty(character_grid)

    degree = len(character_grid)

    validate_grid_is_square(character_grid, degree)

    words_found = set()

    for i in range(0, len(character_grid)):
        for j in range(0, len(character_grid[i])):
            path = [(i, j)]
            stack = deque()
            stack.append(path)

            while stack:
                # TODO: path should probably be an ordered set
                path = stack.pop()
                word = convert_path_to_word(character_grid, path)

                if is_word(word):
                    words_found.add(word)

                terminus = path[-1]
                path_nodeset = set(path)

                for neighbor in get_neighbors(terminus, degree, path_nodeset):
                    stack.extend([path + [neighbor]])

    return words_found


def convert_path_to_word(character_grid: CharGrid, path: List[Tuple[int, int]]) -> str:
    return ''.join(character_grid[p[0]][p[1]] for p in path)


def validate_grid_not_empty(character_grid: CharGrid) -> None:
    if len(character_grid) == 0:
        raise ValueError("A grid should have elements, my friend.")


def validate_grid_is_square(character_grid: CharGrid, height: int) -> None:
    for row in character_grid:
        width = len(row)

        if height != width:
            raise ValueError("A grid ought to be square, no?")


def get_neighbors(point: Tuple[int, int], degree: int, blacklist: Set[Tuple[int, int]]) -> List[Tuple[int, int]]:
    neighbors = []
    for delta in DIRECTIONS:
        potential = sum_pairwise(point, delta)

        if potential in blacklist or any([p < 0 or p >= degree for p in potential]):
            continue

        neighbors.append(potential)

    return neighbors

