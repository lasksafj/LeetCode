class Solution:
    def addMinimum(self, word: str) -> int:
#         split the original work into k strict increasing subarray
        prev = 'z'
        k = 0
        for c in word:
            if c <= prev:
                k += 1
            prev = c
        return k*3 - len(word)