UNDER_TWENTY = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
    "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
    "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
TENS = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
MULTIPLIERS = ["Thousand", "Million", "Billion", "Trillion"]
MULTIPLIER_PARTITION_SIZE = 3

class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        words = []
        digits = count_digits(num)
        pivot = digits % MULTIPLIER_PARTITION_SIZE
        position = digits - pivot
        partitioned_num = num // 10 ** position
        while position >= 0:
            if partitioned_num:
                modulate_number(partitioned_num, words)
                if position >= 3:
                    words.append(MULTIPLIERS[(position // 3) - 1])
            num -= partitioned_num * 10 ** position
            position -= MULTIPLIER_PARTITION_SIZE
            partitioned_num = num // 10 ** position

        print(words)

def modulate_number(num, words):
    if num < 20:
        words.append(UNDER_TWENTY[num])
    elif num < 100:
        words.append(TENS[(num // 10) - 2])
        words.append(UNDER_TWENTY[num % 10])
    elif num < 1000:
        words.append(UNDER_TWENTY[num // 100])
        words.append("Hundred")
        modulate_number(num % 100, words)

def count_digits(num):
    count = 0
    while num:
        num //= 10
        count += 1
    return count

def test():
    s = Solution()
    s.numberToWords(1210543)
    s.numberToWords(12345)
    s.numberToWords(1234567891)
    s.numberToWords(123)

test()
