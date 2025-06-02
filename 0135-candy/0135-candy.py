class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        res = N
        i = 1
        while i < N:
            while i < N and ratings[i] == ratings[i-1]:
                i += 1
                continue
            peak = 0
            while i < N and ratings[i] > ratings[i-1]:
                peak += 1
                res += peak
                i += 1
            if i == N:
                break
            valley = 0
            while i < N and ratings[i] < ratings[i-1]:
                valley += 1
                res += valley
                i += 1
            res -= min(peak, valley)
        return res