class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0]*n
        pre[0] = nums[0]
        for i in range(1,n):
            pre[i] = pre[i-1] + nums[i]
        res = []
        s = sum(nums)
        for i in range(n):
            res.append( abs((pre[i-1] if i>0 else 0) - (s-pre[i])) )
        return res