class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        s = set()
        res = 0
        for n in nums:
            if n in s:
                res ^= n
            s.add(n)
        return res