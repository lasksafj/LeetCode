class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        A = sorted(Counter(s).values())
        return sum(A[:max(0, len(A)-k)])