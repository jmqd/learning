from core import Trie
from core import Node
import logging
import re

def init():
    logging.basicConfig(level=logging.INFO)

def prepare_text(file_location):
    words_pattern = re.compile(r'[^A-Za-z\s]')
    with open(file_location, 'r') as f:
        text = words_pattern.sub('', f.read())
        words = [w.lower() for w in text.split()]
    return words

def build_trie():
    words = prepare_text('text.txt')
    trie = Trie(words)
    logging.info('Trie built.')
    return trie

def test_exists(trie):
    checks = {
            'alice': True,
            'jordan': False,
            'beautifully': True,
            'knelt': True
            }
    for k, v in checks.iteritems():
        print 'Supposed to be {}, returned {}'.format(v, trie.check_exists(k))

def main():
    init()
    trie = build_trie()
    test_exists(trie)

if __name__ == '__main__':
    main()
