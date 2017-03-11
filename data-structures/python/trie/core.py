class Trie(object):
    '''The main Trie object.'''
    def __init__(self, words):
        '''Takes the text given and creates a Trie.'''
        self.root = Node(None, '')
        self.words = words
        self.build(words)

    def build(self, text):
        '''Encapsulates all of the preprocessing build logic.'''
        for word_index, word in enumerate(self.words):
            node = self.root
            for i in xrange(0, len(word)):
                if word[i] not in node.successors:
                    node.add(word[i])
                node = node.successors[word[i]]
            node.word = self.words[word_index]


    def check_exists(self, word):
        '''In the Trie, check if a given word exists.'''
        node = self.root
        for i in xrange(0, len(word)):
            if word[i] not in node.successors:
                return False
            node = node.next(word[i])
        return True

    def add(self, word):
        '''Add a word to the Trie.'''
        self.words.append(word)
        node = self.root
        for i in xrange(0, len(word)):
            if word[i] not in node.successors:
                node.add(word[i])
            node = node.next(word[i])
        node.word = self.words[-1]

class Node(object):
    '''The nodes, which are characters in the english alphabet, [A-Za-z].'''
    def __init__(self, predecessor, char):
        '''Initialize node. Need its predecessor and the char it represents.'''
        self.char = char
        self.word = None
        self.predecessor = predecessor
        self.successors = dict()

    def add(self, char):
        '''Add a char to a node. If it's already there, it doesn't bother.'''
        if char in self.successors:
            return
        self.successors[char] = Node(self, char)

    def next(self, char):
        return self.successors.get(char, None)
