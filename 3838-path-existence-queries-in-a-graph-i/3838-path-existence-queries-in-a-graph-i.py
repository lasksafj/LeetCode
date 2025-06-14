class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        f = list(range(n))
        for i in range(1, n):
            if nums[i] - nums[i-1] <= maxDiff:
                f[i] = f[i-1]
        res = []
        for a,b in queries:
            res.append(f[b] == f[a])
        return res