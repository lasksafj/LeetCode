class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = Counter(a % 3 for a in stones)
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0
        return abs(cnt[1] - cnt[2]) > 2