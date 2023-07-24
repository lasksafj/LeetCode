class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def check(x):
            a = int(sqrt(x))
            return a*a == x
        nums.sort()
        n = len(nums)
        s = set()
        def sol(prev):
            # print(prev)
            if len(s) == len(nums):
                return 1
            i = 0
            res = 0
            while i < n:
                if i in s:
                    i += 1
                    continue
                j = i
                while j < n-1 and nums[j] == nums[j+1]:
                    j += 1
                if len(s) == 0 or check(prev+nums[i]):
                    s.add(i)
                    res += sol(nums[i])
                    s.remove(i)
                i = j+1
            return res
        return sol(0)