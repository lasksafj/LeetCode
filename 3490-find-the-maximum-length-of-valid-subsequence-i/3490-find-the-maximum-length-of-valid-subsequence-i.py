class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd = even = alter = 0
        prev = -1
        for a in nums:
            a &= 1
            if a:
                odd += 1
            else:
                even += 1
            if a != prev:
                alter += 1
            prev = a
        return max(odd, even, alter)