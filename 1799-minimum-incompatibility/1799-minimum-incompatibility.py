class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        size = N//k
        @cache
        def dfs(mask, i, prev, mi, d):
            if d == size:
                return dfs(mask, 0, -1, -1, 0) + nums[prev] - nums[mi]
            if mask == (1<<N )- 1:
                return 0
            res = inf
            while i < N:
                if (1<<i)&mask or (prev>=0 and nums[i] == nums[prev]):
                    i += 1
                    continue
                res = min(res, dfs(mask^(1<<i), i+1, i, mi if mi>=0 else i, d+1))
                if prev == -1:
                    break
                i += 1
            return res
        res = dfs(0, 0, -1, -1, 0)
        return res if res < inf else -1
