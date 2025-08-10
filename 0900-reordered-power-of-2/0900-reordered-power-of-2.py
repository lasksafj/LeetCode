class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n = sorted(str(n))
        for i in range(32):
            if sorted(str(1<<i)) == n:
                return True
        return False