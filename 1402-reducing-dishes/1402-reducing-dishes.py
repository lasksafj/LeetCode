class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        s,res = 0,0
        for n in satisfaction:
            s += n
            if s < 0:
                s = 0
            res += s
        return res
        
        