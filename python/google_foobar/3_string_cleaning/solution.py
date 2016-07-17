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
    if not occurences and chunk not in potentials:
        return chunk
    if occurences:
        for occurence in occurences:
            chunk_instance = remove_slice(chunk, len(word), occurence)
            potential = decode_chunk(chunk_instance, word, potentials)
            if potential and potential not in potentials:
                potentials.append(potential)

def rank_potentials(potentials):
    potentials.sort(key = len)
    final_potentials = []
    length = potentials[0]
    for potential in potentials:
        if length < len(potential):
            break
        final_potentials.append(potential)
    final_potentials.sort()
    return final_potentials[0]

def answer(chunk, word):
    potentials = []
    decode_chunk(chunk, word, potentials)
    return rank_potentials(potentials)

