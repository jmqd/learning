from operator import itemgetter

def sort_intervals_by_start_time(intervals):
    return sorted(intervals, key = itemgetter(0))

def answer(intervals):
    time_watched = 0
    intervals = sort_intervals_by_start_time(intervals)
    prev_interval = None
    for interval in intervals:
        if prev_interval and prev_interval[1] > interval[0]:
            interval[0] = prev_interval[1]
        time_watched += interval[1] - interval[0]
        prev_interval = interval
    return time_watched
