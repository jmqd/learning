class Trie(object):
    '''The main Trie object.'''
    def __init__(self, words):
        '''Takes the text given and creates a Trie.'''
        self.root = Node(None, '^')
        self.words = words
        self.build(words)

    def build(self, text):
        for word_index, word in enumerate(self.words):
            node = self.root
            for i in xrange(0, len(word)):
                if word[i] in node.successors:
                    node = node.successors[word[i]]
                else:
                    node.add(word[i])
                    node = node.successors[word[i]]
            node.word = self.words[word_index]

    def check_exists(self, word):
        node = self.root
        for i in xrange(0, len(word)):
            if word[i] in node.successors:
                node = node.successors[word[i]]
            else:
                return False
        return True

class Node(object):
    '''The nodes, which are characters in the english alphabet, [A-Za-z].'''
    def __init__(self, predecessor, char):
        self.char = char
        self.word = None
        self.predecessor = predecessor
        self.successors = dict()

    def add(self, char):
        if char in self.successors:
            return
        self.successors[char] = Node(self, char)
