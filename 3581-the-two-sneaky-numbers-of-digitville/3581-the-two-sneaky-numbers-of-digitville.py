class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a = 0
        z = 0
        for n in nums:
            a ^= n
            z += n == 0
        for i in range(1, len(nums)-2):
            a ^= i
        if z == 2:
            return [0,a]
        d = a&(-a)
        r1 = 0
        for n in nums:
            if n&d:
                r1 ^= n
        for i in range(1, len(nums)-2):
            if i&d:
                r1 ^= i
        return [r1,a^r1]