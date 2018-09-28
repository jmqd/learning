from collections import Counter

class Solution:
    def getHint(self, secret, guess):
        guess_counter, secret_counter = Counter(guess), Counter(secret)
        bulls = 0
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bulls += 1
                secret_counter[secret[i]] -= 1
                guess_counter[secret[i]] -= 1

        cows = 0
        for char, count in secret_counter.items():
            guess_count = guess_counter.get(char, 0)
            cows += min(count, guess_count)

        return str(bulls) + "A" + str(cows) + "B"
