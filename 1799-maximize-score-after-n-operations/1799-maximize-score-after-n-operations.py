class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def sol(mask, no_pairs):
            if no_pairs*2 == n:
                return 0
            res = 0
            for i in range(n):
                if nums[i] == 0:
                    continue
                for j in range(i+1,n):
                    if nums[j] == 0:
                        continue
                    a,b = nums[i],nums[j]
                    nums[i],nums[j] = 0,0
                    no_pairs += 1
                    mask ^= (1 << i)
                    mask ^= (1 << j)
                    res = max(res, (no_pairs)*gcd(a,b) + sol(mask, no_pairs))
                    nums[i],nums[j] = a,b
                    no_pairs -= 1
                    mask ^= (1 << i)
                    mask ^= (1 << j)
                
            return res
        mask = pow(2,n)-1
        return sol(mask, 0)