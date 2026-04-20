class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        N = len(colors)
        res = 0
        for i in range(N):
            j = N-i-1
            if colors[j] != colors[0]:
                res = max(res, j)
            elif colors[i] != colors[-1]:
                res = max(res, N-i-1)
        return res