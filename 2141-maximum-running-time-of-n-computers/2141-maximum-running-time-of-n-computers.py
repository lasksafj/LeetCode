class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse=True)
        a = sum(batteries[:n])
        b = sum(batteries) - a

        for c in batteries[:n]:
            if b >= c*n - a:
                return (b+a)//n
            a -= c
            n -= 1
        return batteries[-1]
        # c*n <= b+a
        # c <= (b+a)/n

        