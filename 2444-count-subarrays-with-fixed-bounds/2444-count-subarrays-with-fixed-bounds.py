class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        if minK > maxK:
            return 0
        a,b,c = -1,-1,-1
        res = 0
        for i,n in enumerate(nums):
            if (n == minK or n == maxK):
                if minK == maxK:
                    b = c = i
                elif c == -1 or nums[c] != n:
                    b,c = c,i
                else:
                    c = i
            elif n < minK or n > maxK:
                a,b,c = [i]*3
            res += b-a
        return res