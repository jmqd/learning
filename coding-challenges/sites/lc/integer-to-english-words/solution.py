from math import log, floor

UNDER_TWENTY = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
    "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
    "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
TENS = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
MULTIPLIERS = ["Hundred", "Thousand", "Million", "Billion", "Trillion"]

class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        words = []
        modulate_number(num, words)
        print(words)

def modulate_number(num, words):
        modulator = 10
        while num > 999:
            remainder = num % modulator
            num -= remainder
            modulator *= 10
            print(remainder)

            if not remainder:
                continue

            order = floor(log(remainder + 1, 10))
            print("Order of remainder is: {}".format(order))

            if remainder < 20:
                words.append(UNDER_TWENTY[remainder])
            elif order == 1:
                words.append(TENS[(remainder // 10) - 2])
            elif order == 2:
                print("ALERT", order, remainder)
            elif order > 3:
                print("remainder // modulator = ", remainder // 1000)
                words.append(MULTIPLIERS[order - 4])

def test():
    s = Solution()
    s.numberToWords(1210543)

test()
