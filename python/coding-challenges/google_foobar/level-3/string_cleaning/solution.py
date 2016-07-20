from collections import deque

def get_occurences(chunk, word):
    start = 0
    while True:
        start = chunk.find(word, start)
        if start > -1:
            yield (start, start + len(word),)
            start += 1
        else:
            break

def remove_slice(chunk, start, end):
    return chunk[:start] + chunk [end:]

def decode_chunk(chunk, word):
    answer = chunk
    seen = set()
    queue = deque([chunk])

    while len(queue):
        value = queue.popleft()
        matches = get_occurences(value, word)
        for start, end in matches:
            potential = remove_slice(value, start, end)
            if potential in seen:
                continue
            elif len(potential) == len(answer):
                answer = min(answer, potential)
            elif len(potential) < len(answer):
                answer = potential
            seen.add(potential)
            queue.append(potential)
    return answer

def answer(chunk, word):
    return decode_chunk(chunk, word)

