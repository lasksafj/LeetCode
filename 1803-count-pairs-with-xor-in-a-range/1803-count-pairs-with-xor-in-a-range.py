class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        L = 15
        def add(n,T):
            cur = T
            n |= 1<<L
            for ch in bin(n)[3:]:
                ch = int(ch)
                if ch not in cur:
                    cur[ch] = {}
                cur = cur[ch]
                cur['cnt'] = cur.get('cnt', 0) + 1
        
        def calc(n, k, T):
            n |= 1<<L
            k |= 1<<L
            k = bin(k)[3:]
            j = 0
            cur = T
            res = 0
            
            for ch in bin(n)[3:]:
                ch = int(ch)
                if k[j] == '0':
                    if ch not in cur:
                        return res
                    cur = cur[ch]
                else:
                    if ch in cur:
                        res += cur[ch].get('cnt', 0)
                    ne = ch^1
                    if ne not in cur:
                        return res
                    cur = cur[ne]
                j += 1
            return res
        
        def sol(k, T):
            res = 0
            for n in nums:
                res += calc(n, k, T)
                add(n, T)
            return res
        return sol(high+1, {}) - sol(low, {})
