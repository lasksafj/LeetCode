class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        nozero = 0
        for n in nums:
            if n == 0:
                nozero += 1
            else:
                p *= n
        if nozero > 1:
            return [0]*len(nums)
        res = []
        for n in nums:
            if n == 0:
                res.append(p)
            elif nozero:
                res.append(0)
            else:
                res.append(p//n)
        return res