class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        N = len(colors)
        for i in range(N):
            j = N-i-1
            if colors[j] != colors[0] or colors[i] != colors[-1]:
                return N-i-1
        return 0