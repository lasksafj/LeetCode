class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        def dfs(n):
            if low <= n <= high:
                res.append(n)
            if n > high or n%10 == 9:
                return
            dfs(n*10 + n%10 + 1)
        for n in range(1, 10):
            dfs(n)
        return sorted(res)