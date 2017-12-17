LOWER_BOUND = -2147483648
UPPER_BOUND = 2147483647

def solve(i: int) -> int:
    base = 10
    digit_arr = []
    mult = 1 if i > 0 else -1
    num = abs(i)

    while num:
        digit_arr.append(num % base)
        num //= base

    reverse_num = 0
    for digit in digit_arr[::-1]:
        reverse_num += mult * digit
        mult *= base

    return reverse_num if LOWER_BOUND <= reverse_num <= UPPER_BOUND else 0


def execute_tests() -> None:
    simple_case_123 = (123, 321)
    simple_case_321 = (321, 123)
    long_case_453412 = (453412, 214354)
    zero = (0, 0)
    one = (1, 1)
    min_allowed = (-8463847412, -2147483648)
    too_small = (-9463847412, 0)
    too_big = (1534236469, 0)

    for test_case in [
            simple_case_123,
            simple_case_321,
            long_case_453412,
            zero,
            one,
            min_allowed,
            too_small,
            too_big
            ]:
        test(*test_case)

def test(i: int, expected: int) -> None:
    answer = solve(i)
    print(i, "reversed is", answer, "expected:", expected)
    assert answer == expected

def main() -> None:
    return execute_tests()

if __name__ == '__main__':
    main()
