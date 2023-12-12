class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a,b = 0,0
        for n in nums:
            if n > a:
                b = a
                a = n
            else:
                b = max(b,n)
        return (a-1)*(b-1)