class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = set()
        def sol(cur):
            if cur == len(nums):
                if len(path) >= 2:
                    res.add(tuple(path))
                return
            if not path or nums[cur] >= path[-1]:
                path.append(nums[cur])
                sol(cur+1)
                path.pop()
            sol(cur+1)
        sol(0)
        return list(res)