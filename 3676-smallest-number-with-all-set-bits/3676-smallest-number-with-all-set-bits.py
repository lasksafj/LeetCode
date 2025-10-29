class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1<<(len(bin(n)[2:]))) - 1