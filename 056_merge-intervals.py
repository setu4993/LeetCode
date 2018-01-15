# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        sol = []
        intervals.sort(key=lambda i: i.start)
        for interval in intervals:
            if sol and interval.start <= sol[-1].end:
                sol[-1].end = max(sol[-1].end, interval.end)
            else:
                sol.append(interval)
        return sol


def PrintInterval(intervals):
    string = ''
    for i in intervals:
        string += "[" + str(i.start) + ', ' + str(i.end) + "]"
    return string

print(PrintInterval(Solution().merge([Interval(3, 8), Interval(2, 6), Interval(8, 10), Interval(15, 18)])))