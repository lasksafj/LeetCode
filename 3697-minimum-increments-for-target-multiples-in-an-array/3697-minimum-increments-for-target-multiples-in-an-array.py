class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        N = len(nums)
        T = len(target)
        @cache
        def dfs(i, mask):
            if i == len(nums):
                return 0 if mask == 0 else inf
            res = dfs(i+1, mask)
            for sub_mask in range(1<<T):
                if sub_mask & mask == sub_mask:
                    d = 1
                    for j in range(T):
                        if (1<<j) & mask and (1<<j) & sub_mask == 0:
                            d = lcm(d, target[j])
                    op = (d - nums[i] % d) % d
                    res = min(res, dfs(i+1, sub_mask) + op)
            return res
        return dfs(0, (1<<T) - 1)