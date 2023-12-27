class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        i = 0
        while i < len(colors):
            j = i
            ma = neededTime[j]
            s = neededTime[j]
            while j+1 < len(colors) and colors[j] == colors[j+1]:
                ma = max(ma, neededTime[j+1])
                s += neededTime[j+1]
                j += 1
            res += s - ma
            i = j+1
        return res