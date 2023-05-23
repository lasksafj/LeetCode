class Solution:
    def punishmentNumber(self, n: int) -> int:
        def dfs(i, prev, cur, a, target):
            if i == len(a):
                return cur == target
            s = cur
            s -= prev
            prev = prev*10 + a[i]
            s += prev
            if dfs(i+1, prev, s, a, target):
                return True
            s = cur
            s += a[i]
            prev = a[i]
            return dfs(i+1, prev, s, a, target)
        res = 0
        for target in range(1, n+1):
            b = target*target
            a = []
            while b > 0:
                a.append(b%10)
                b //= 10
            a = a[::-1]
            if dfs(0, 0, 0, a, target):
                res += target*target
        return res
            