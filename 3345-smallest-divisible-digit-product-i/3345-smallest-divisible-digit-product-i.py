class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while n % 10 != 0:
            a = prod(int(i) for i in str(n))
            if a % t == 0:
                return n
            n += 1
        return n