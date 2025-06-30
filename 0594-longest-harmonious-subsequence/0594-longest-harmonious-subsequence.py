class Solution:
    def findLHS(self, nums: List[int]) -> int:
        A = sorted(Counter(nums).items(), key=lambda x:x[0])
        res = 0
        for i in range(len(A)-1):
            if A[i+1][0] - A[i][0] == 1:
                res = max(res, A[i+1][1] + A[i][1])
        return res