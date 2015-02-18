# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval

    def merge(self, intervals):
        if not intervals:
            return []
        res = []
        intervals = sorted([[i.start, i.end] for i in intervals])
        prev = intervals[0]
        for i in xrange(1, len(intervals)):
            if intervals[i][0] <= prev[1]:
                prev[1] = max(prev[1], intervals[i][1])
            else:
                res.append(prev)
                prev = intervals[i]
        res.append(prev)
        return res
