class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        a,b = startPos
        c,d = homePos
        if a > c:
            a,c = c,a
        res = sum(rowCosts[a:c+1]) - rowCosts[startPos[0]]
        if b > d:
            b,d = d,b
        res += sum(colCosts[b:d+1]) - colCosts[startPos[1]]
        return res