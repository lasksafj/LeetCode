class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        a = 0
        for n in nums:
            a ^= n
        return bin(a^k).count('1')