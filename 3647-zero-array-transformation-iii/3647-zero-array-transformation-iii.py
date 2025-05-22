class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        N = len(nums)
        M = len(queries)
        A = [0]*(N+1)
        SL = SortedList()
        res = 0
        cur = 0
        j = 0
        for i in range(N):
            cur += A[i]
            while SL and SL[0] < i:
                SL.pop(0)
            while j < M and queries[j][0] <= i:
                SL.add(queries[j][1])
                j += 1
            while SL and cur < nums[i]:
                cur += 1
                A[SL.pop()+1] -= 1
                res += 1
            if cur < nums[i]:
                return -1
        return M - res