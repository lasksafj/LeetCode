class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        ma = max(milestones)
        s = sum(milestones)
        if ma > s-ma:
            return (s-ma)*2+1
        return s