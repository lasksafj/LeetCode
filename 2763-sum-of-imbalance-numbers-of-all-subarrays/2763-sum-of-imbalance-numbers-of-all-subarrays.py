class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            s = set()
            s.add(nums[i])
            cur = 0
            for j in range(i+1, n):
                v = nums[j]
                if v not in s:
                    d = 1
                    if v+1 in s:
                        d -= 1
                    if v-1 in s:
                        d -= 1
                    s.add(v)
                    cur += d
                res += cur
        return res