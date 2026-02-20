"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        A = []
        for emp in schedule:
            for interval in emp:
                A.append([interval.start, 1])
                A.append([interval.end, -1])
        A.sort(key=lambda x:[x[0], -x[1]])
        res = []
        p_bal = 0
        prev = -inf
        for t,op in A:
            if p_bal == 0 and prev > -inf:
                res.append(Interval(prev, t))
            p_bal += op
            prev = t
        return res