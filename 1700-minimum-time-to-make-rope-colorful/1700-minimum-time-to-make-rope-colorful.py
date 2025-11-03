class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = 0
        N = len(colors)
        res = 0
        while i < N:
            j = i+1
            while j < N and colors[j] == colors[i]:
                j += 1
            res += max(neededTime[i:j])
            i = j
        return sum(neededTime) - res