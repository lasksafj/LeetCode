class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        m, n = k.bit_length(), len(receiver)
        # pos[i][j] means the end point after move 2^i steps from j
        pos = [[receiver[j] for j in range(n)] for i in range(m)]
        # profit[i][j] means the profit after move 2^i steps from j, not include j itself
        profit = [[receiver[j] for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(n):
                x = pos[i-1][j]
                pos[i][j] = pos[i-1][x]
                profit[i][j] = profit[i-1][j] + profit[i-1][x]
        def F(now, p):
            if p == -1: return 0
            if (k & (1 << p)) == 0: return F(now, p - 1)
            return profit[p][now] + F(pos[p][now], p - 1)

        return max([F(i, m - 1) + i for i in range(n)])