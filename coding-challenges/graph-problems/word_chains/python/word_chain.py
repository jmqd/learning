import Graph, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dictionary', default='dictionary.txt')
args = parser.parse_args()

def build_dictionary(words):
    dictionary = {}
    for word in words:
        dictionary[word] = []
    while len(words) > 0:
        word = words.pop()
        for word_i in words:
            if is_chainable(word, word_i):
                dictionary[word].append(word_i)
                dictionary[word_i].append(word)
    return dictionary


def is_chainable(string_1, string_2):
    if len(string_1) != len(string_2):
        return False
    difference = False
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            if difference:
                return False
            difference = True
    if difference:
        return True
    return False

def import_words(filename):
    words = []
    with open(filename, 'r') as f:
        lines = (line for line in f)
        for row in lines:
            words.append(row.strip())
    return words

words = import_words(args.dictionary)
dictionary = build_dictionary(words)
graph = Graph.Graph(dictionary)
graph.show()
while True:
    word_from = input("From: ")
    word_to = input("To: ")
    print(graph.search(word_from, word_to))

