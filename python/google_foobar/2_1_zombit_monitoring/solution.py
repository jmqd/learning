from operator import itemgetter

intervals = [[1, 100], [4, 10], [4, 18], [19, 20], [19, 20], [13, 20], [50, 60]]

def sort_intervals_by_start_time(intervals):
    return sorted(intervals, key = itemgetter(0))

def answer(intervals):
    time_watched = 0
    intervals = sort_intervals_by_start_time(intervals)
    prev_interval = None
    for interval in intervals:
        if prev_interval:
            if prev_interval[1] > interval[0]:
                interval[0] = prev_interval[1]
                if interval[0] > interval[1]:
                    continue
        time_watched += interval[1] - interval[0]
        prev_interval = interval
    return time_watched

answer(intervals)
