class Solution:
    def numberOfWays(self, corridor: str) -> int:
        N = len(corridor)
        mod = 10**9+7
        ns = 0
        A = []
        i = 0
        while i < N:
            if ns == 2:
                ns = 0
            ns += corridor[i] == 'S'
            if ns < 2:
                i += 1
            else:
                j = i+1
                while j < N and corridor[j] == 'P':
                    j += 1
                if j < N:
                    A.append(j-i-1)
                i = j
        if ns < 2:
            return 0
        res = 1
        for n in A:
            res = (res*(n+1)) % mod
        return res