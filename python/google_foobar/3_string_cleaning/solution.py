def get_occurences(chunk, word):
    start = 0
    starts = []
    while True:
        start = chunk.find(word, start) + 1
        if start > 0:
            starts.append(start - 1)
        else:
            return starts

def remove_slice(chunk, length, begin):
    chunk = chunk[:begin] + chunk[begin + length:]
    return chunk


def decode_chunk(chunk, word, potentials):
    occurences = get_occurences(chunk, word)
    if not occurences:
        potentials.append(chunk)
    if occurences:
        for occurence in occurences:
            chunk_instance = remove_slice(chunk, len(word), occurence)
            decode_chunk(chunk_instance, word, potentials)

def rank_potentials(potentials):
    minimum = min(map(len, potentials))
    for potential in potentials:
        if len(potential) != minimum:
            potentials.remove(potential)
    potentials.sort()
    return potentials[0]

def answer(chunk, word):
    potentials = []
    decode_chunk(chunk, word, potentials)
    return rank_potentials(potentials)

