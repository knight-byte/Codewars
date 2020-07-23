def sum_of_intervals(intervals):
    return len(set(i for s, e in intervals for i in range(s, e)))
