import sys
import enchant
from typing import List, Set

sys.path.insert('../src/')
from solution import solve

TEST_BOARDS_AND_SOLUTIONS_FILE = 'data.json'
EXAMPLE_BOARDS = json.load(TEST_BOARDS_AND_SOLUTIONS_FILE)
english_dictionary = enchant.dict('en_US')

def test_example_boards():
    for name, data in TEST_DATA.items():
        assert solve(data['board'], english_dictionary.check) == data['correct_answer']

