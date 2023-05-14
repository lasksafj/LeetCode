class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        no_pairs = [0]
        @cache
        def sol(mask):
            if no_pairs[0]*2 == n:
                return 0
            res = 0
            for i in range(n):
                if (1 << i) & mask:
                    continue
                for j in range(i+1,n):
                    if (1 << j) & mask:
                        continue
                    no_pairs[0] += 1
                    nmask = mask | (1 << i) | (1 << j)
                    res = max(res, (no_pairs[0])*gcd(nums[i],nums[j]) + sol(nmask))
                    no_pairs[0] -= 1
            return res
        mask = pow(2,n)
        return sol(mask)