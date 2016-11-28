from __future__ import print_function
import re

def to_military(time):
    ampm_regex = re.compile(r'(^\d{2})(:\d{2}:\d{2})([A-Za-z]{2})')
    hours, mins_and_secs, time_period = ampm_regex.findall(time)[0]
    military_time = (hours.zfill(2) if time_period == 'AM' else str((int(hours)
        + 12) % 24).zfill(2)) + mins_and_secs
    return military_time

def hackerrank_solve():
    time = raw_input().strip()
    print(to_military(time))

def main():
    test()

def test():
    cases = [
        '11:32:32AM',
        '04:41:11PM',
        '12:51:21PM',
        '07:21:41PM',
        '01:41:12AM'
        ]
    for case in cases:
        print(to_military(case))

if __name__ == '__main__':
    main()
