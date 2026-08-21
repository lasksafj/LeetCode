class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        N = len(coins)
        mp = {}
        for mask in range(1, 1<<N):
            s = 1
            for i,c in enumerate(coins):
                if mask&(1<<i):
                    s = lcm(s, c)
            mp[mask] = s
        l,r = min(coins), max(coins)*k
        res = 0
        while l <= r:
            x = (l+r)//2
            d = 0
            for mask in range(1, 1<<N):
                s = x // mp[mask]
                if bin(mask).count('1') & 1:
                    d += s
                else:
                    d -= s
            if d > k:
                r = x-1
            elif d < k:
                l = x+1
            else:
                mi = x
                for c in coins:
                    if x%c < mi:
                        mi = x%c
                        res = c * (x//c)
                break
        return res