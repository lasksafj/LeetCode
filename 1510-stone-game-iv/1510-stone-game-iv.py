class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # state with remaining stone i after end of current player turn
        @cache
        def dfs(i):
            # rem stone = 0 after current player move => current player lose
            if i == 0: return False

            for k in range(int(sqrt(i)), 0, -1):
                if not dfs(i-k*k):
                    return True
            return False
        return dfs(n)