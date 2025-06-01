class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        ODD = [i for i in range(1, n+1) if i&1]
        EVEN = [i for i in range(1, n+1) if i&1==0]
        A = [EVEN] + [ODD]
        res = []
        if n&1:
            t = perm(len(ODD), len(ODD)) * perm(len(EVEN), len(EVEN))
            if k > t: return []
            nt = t // len(ODD)
            val = A[1][ceil(k/nt) - 1]
        else:
            t = perm(len(EVEN), len(EVEN)) ** 2 * 2
            if k > t: return []
            nt  = t // n
            val = ceil(k/nt)
        
        A[val&1].remove(val)
        res.append(val)
        t = nt
        k %= nt

        for i in range(2,n+1):
            parity = val&1^1
            nt = t//len(A[parity])
            val = A[parity][ceil(k/nt) - 1]
            A[parity].remove(val)
            res.append(val)
            t = nt
            k %= nt
        return res
