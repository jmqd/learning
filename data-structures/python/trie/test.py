from collections import OrderedDict
from core import Trie
from core import Node
import tabulate
import logging
import re

GENERIC_WORD_TEST_CASES = OrderedDict(
            alice = True,
            wonderland = False,
            jordan = False,
            beautifully = True,
            knelt = True,
            hello = False,
            presently = True,
            inconceivable = False
            )

WORDS_TO_ADD = ['indomitable', 'equanimity', 'leah', 'michael', 'alice']

def init():
    logging.basicConfig(level=logging.INFO)

def prepare_text(file_location):
    words_pattern = re.compile(r'[^A-Za-z\s]')
    with open(file_location, 'r') as f:
        text = words_pattern.sub(' ', f.read())
        words = [w.lower() for w in text.split()]
    return words

def build_trie():
    words = prepare_text('text.txt')
    trie = Trie(words)
    logging.info('Trie built.')
    return trie

def test_exists(trie, test_cases):
    print '=' * 79
    print 'Testing existence of various words in Trie'
    print '=' * 79
    table = [[]] * len(test_cases)
    index = 0
    for k, v in test_cases.iteritems():
        check = trie.check_exists(k)
        status = 'PASS' if (v == check) else 'FAIL'
        table[index] = [k, status, v, check]
        assert v == check
        index += 1
    print tabulate.tabulate(table,
            ['word', 'status', 'expected', 'actual'],
            tablefmt = 'fancy_grid')
    print '*' * 60
    print 'All existence checks passed.'
    print '*' * 60

def test_adding(trie, words):
    print '=' * 79
    print 'Testing the additon of words the Trie'
    print '=' * 79
    for word in words:
        trie.add(word)
        print 'added', word
    print '*' * 60
    print 'All words seemed to successfully add... Testing that...'
    print '*' * 60
    test_exists(trie, {word:True for word in words})

def main():
    init()
    trie = build_trie()
    test_exists(trie, GENERIC_WORD_TEST_CASES)
    test_adding(trie, WORDS_TO_ADD)

if __name__ == '__main__':
    main()
