class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        N = len(nums)
        for i in range(N-1, -1, -1):
            a,b = 0,i-1
            n = nums[i]
            ans = 0
            while a < b:
                if nums[a] + nums[b] <= n:
                    a += 1
                else:
                    ans += b-a - (a <= i <= b)
                    b -= 1
            res += ans
        return res