class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        c = 1
        for i in range(len(digits)):
            digits[i] += c
            c = digits[i]//10
            digits[i] %= 10
        return ((digits + [c]) if c else digits)[::-1]