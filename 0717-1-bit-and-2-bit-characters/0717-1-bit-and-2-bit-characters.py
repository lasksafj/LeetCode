class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bits = bits[:-1]
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == len(bits)