'''
Naive first approach w/o DP. Likely many optimizations to be made w/ DP.
'''

from typing import List

def find_substrings(w: str) -> List[str]:
    return [w[i:j + 1] for i in range(len(w)) for j in range(i, len(w))]

def gatekeep(word: str) -> str:
    for i in range(len(word)):
        if word[i] != word[-i - 1]:
            return ''
    return word

def solve(word: str) -> str:
    substrings = find_substrings(word)
    max_seen = ''
    for word in substrings:
        palindrome = gatekeep(word)
        if len(palindrome) > len(max_seen):
            max_seen = palindrome
    return max_seen

def main() -> None:
    words = ['dad', 'happy', 'radar', 'timeless', 'asdsadasd', 'dbbc']
    for w in words:
        print("Longest palindromic substr for {}: {}".format(w, solve(w)))

if __name__ == '__main__':
    main()

