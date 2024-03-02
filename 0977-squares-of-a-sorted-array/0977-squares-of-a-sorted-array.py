class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        cnt = [0]*(max(abs(min(nums)), abs(max(nums)))+1)
        for n in nums:
            cnt[abs(n)] += 1
        res = []
        for i in range(len(cnt)):
            res += [i*i] * cnt[i]
        return res