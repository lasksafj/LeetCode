class Solution:
    def sumZero(self, n: int) -> List[int]:
        A = list(range(1, n//2+1))
        return A + [-a for a in A] + ([0] if n&1 else [])