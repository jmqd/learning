import sys
import enchant
import os
import json
from typing import List, Set, Any

sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))
from solution import solve

TEST_DATA_FILENAME = os.path.join(os.path.dirname(__file__), 'data.json')
english_dictionary = enchant.Dict('en_US')

def test_example_boards():
    test_data = load_json_file(TEST_DATA_FILENAME)
    for name, data in test_data.items():
        assert solve(data['board'], english_dictionary.check) == set(data['correct_answer'])

def load_json_file(filename: str) -> Any:
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

