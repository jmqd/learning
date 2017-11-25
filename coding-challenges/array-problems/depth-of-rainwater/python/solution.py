import typing
from typing import List
from typing import Tuple

def main() -> None:
    points = input("Raw int points of 'island' curve? (comma delim): ")
    line = [int(x) for x in points.split(',')]
    depth_curve = preprocess(line)
    print("Here is the depth curve: {}".format(depth_curve))

    query = None
    while query != '-1':
        query = input("Position to check depth of? (-1 to quit) > ")
        try:
            print("Depth is {}".format(depth_curve[int(query)]))
        except Exception as e:
            print(e)

def preprocess(line: List[int]) -> List[int]:
    left_high_tides = find_high_tides(line)
    right_high_tides = list(reversed(find_high_tides(reversed(line))))
    high_tides = []

    for i, height in enumerate(line):
        high_tide = min(
                left_high_tides[i],
                right_high_tides[i]
                )
        high_tide = max(high_tide - height, 0)
        high_tides.append(high_tide)
    return high_tides

def find_high_tides(line: List[int]) -> List[int]:
    high_tide = 0
    high_tides = []
    for i in line:
        high_tides.append(high_tide)
        high_tide = i if i > high_tide else high_tide
    return high_tides

def test() -> None:
    simple_ascending_case = ([1, 2, 3, 4], [0, 0, 0, 0])
    simple_descending_case = ([4, 3, 2, 1], [0, 0, 0, 0])
    simple_depth_case = ([1, 3, 1, 5, 2], [0, 0, 2, 0, 0])
    nested_depth_case = ([1, 10, 3, 1, 3, 10, 1], [0, 0, 7, 9, 7, 0, 0])
    test_case(*simple_ascending_case)
    test_case(*simple_descending_case)
    test_case(*simple_depth_case)
    test_case(*nested_depth_case)

def test_case(data, expected):
    actual = preprocess(data)
    print(actual)
    assert actual == expected

if __name__ == '__main__':
    main()

