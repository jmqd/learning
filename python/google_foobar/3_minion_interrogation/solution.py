import operator

def answer(minions):
    answer = []
    final_answer = []
    for i in xrange(0, len(minions)):
        minutes = minions[i][0]
        numerator = minions[i][1]
        denominator = minions[i][2]
        value = (numerator / float(denominator)) / float(minutes)
        answer.append((i, value))
    answer.sort(key = operator.itemgetter(0))
    answer.sort(reverse = True, key = operator.itemgetter(1))
    for minion in answer:
        final_answer.append(minion[0])
    return final_answer

