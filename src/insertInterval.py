# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval

    def insert(self, intervals, newInterval):
        res = []
        for i, x in enumerate(intervals):
            if x.start > newInterval.end:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            if x.end < newInterval.start:
                res.append(x)
            else:
                newInterval.start = min(newInterval.start, x.start)
                newInterval.end = max(newInterval.end, x.end)
        res.append(newInterval)
        return res
