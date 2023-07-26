class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        vis = [0]*n
        res = []
        path = []
        def sol(i):
            if i == n:
                res.append(path[:])
                return
            for j in range(n):
                if not vis[j]:
                    path.append(nums[j])
                    vis[j] = 1
                    sol(i+1)
                    path.pop()
                    vis[j] = 0
        sol(0)
        return res