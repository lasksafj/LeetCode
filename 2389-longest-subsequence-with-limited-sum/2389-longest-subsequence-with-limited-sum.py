class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        pre = [0] * n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i-1] + nums[i]
        res = []
        for q in queries:
            a = bisect_right(pre, q)
            res.append(a)
                
        return res