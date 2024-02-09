class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        N = len(nums)
        # @cache
        # def dfs(i,prev):
        #     if i == N:
        #         return []
        #     A = dfs(i+1,prev)
        #     B = []
        #     if prev == -1 or nums[i] % nums[prev] == 0:
        #         B = [nums[i]] + dfs(i+1,i)
        #     return A if len(A) > len(B) else B
        # return dfs(0,-1)

        @cache
        def dfs(i):
            A = []
            for j in range(i+1, N):
                if nums[j]%nums[i] == 0:
                    tmp = dfs(j)
                    if len(tmp) > len(A):
                        A = tmp
            return [nums[i]] + A
        res = []
        for i in range(N):
            tmp = dfs(i)
            if len(tmp) > len(res):
                res = tmp
        return res