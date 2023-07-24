class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        a = numsDivide[0]
        for n in numsDivide:
            a = gcd(a,n)
        res = 0
        for n,v in sorted(Counter(nums).items()):
            if a % n == 0:
                return res
            res += v
        return -1