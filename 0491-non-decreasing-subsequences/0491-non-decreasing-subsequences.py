class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = set()
        n = len(nums)
        def sol(cur, prevNum):
            # print(path)
            if nums[cur] >= prevNum:
                path.append(nums[cur])
                # print(path)
                if len(path) >= 2:
                    res.add(tuple(path))
                for i in range(cur+1, n):
                    sol(i, nums[cur])
                path.pop()
        for i in range(n):
            sol(i, -101)
        return list(res)