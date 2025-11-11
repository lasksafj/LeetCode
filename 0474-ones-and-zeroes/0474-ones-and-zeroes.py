class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0,0,0)}
        for s in strs:
            mp = Counter(s)
            cur = set()
            for n0,n1,k in dp:
                if n0+mp['0'] <= m and n1+mp['1'] <= n:
                    cur.add((n0+mp['0'], n1+mp['1'], k+1))
            dp |= cur
        return max(dp, key=lambda e:e[2])[2]