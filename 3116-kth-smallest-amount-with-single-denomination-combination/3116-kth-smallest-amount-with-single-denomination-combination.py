class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        mp = [0] * 2**len(coins)
        for mask in range(1, 2**len(coins)):
            A = [v for i,v in enumerate(coins) if (1<<i)&mask > 0]
            d = A[0]
            for a in A:
                d = lcm(d,a)
            mp[mask] = d
        
        l,r = 0,k*coins[0]
        while l <= r:
            mi = (l+r)//2
            no = 0
            # inclusion-exclusion principle
            for mask in range(1, 2**len(coins)):
                if bin(mask).count('1') % 2:
                    no += mi//mp[mask]
                else:
                    no -= mi//mp[mask]
            
            if no < k:
                l = mi+1
            elif no > k:
                r = mi-1
            else:
                min_rem = inf
                for c in coins:
                    if mi%c < min_rem:
                        min_rem = mi%c
                        res = mi//c * c
                return res
                        
        return res