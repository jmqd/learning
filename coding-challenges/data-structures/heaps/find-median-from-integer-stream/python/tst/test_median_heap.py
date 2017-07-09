from typing import Any
import json
import sys
import os
import statistics

sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))
from solution import MedianHeap

TEST_INTEGERS = os.path.join(os.path.dirname(__file__), 'test-numbers.json')

def test_median_heap_sample_data() -> None:
    heap = MedianHeap()
    nums = load_jsonfile(TEST_INTEGERS)
    for num in nums:
        heap.push(num)

    assert heap.get_median() == statistics.median(nums)


def load_jsonfile(filename: str) -> Any:
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

