class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        @cache
        def dfs(i, mask):
            if mask == (1<<N)-1:
                return [0, [i]]
            res = []
            cur = inf
            for j in range(N):
                if j != i and (1<<j)&mask == 0:
                    a,B = dfs(j, mask|(1<<j))
                    a += abs(i-nums[j])
                    if mask|(1<<j) == (1<<N)-1:
                        a += abs(j-nums[0])
                    if a < cur:
                        res = [a, [i] + B]
                        cur = a
            return res
        a,B = dfs(0, 1)
        return B