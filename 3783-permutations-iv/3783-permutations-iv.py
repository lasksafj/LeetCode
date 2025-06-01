class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        A = list(range(1, n+1))
        ODD = [i for i in range(1, n+1) if i&1]
        EVEN = [i for i in range(1, n+1) if i&1==0]
        res = []
        if n&1:
            t = perm(len(ODD), len(ODD)) * perm(len(EVEN), len(EVEN))
            if k > t: return []
            nt = t // len(ODD)
            val = ODD[ceil(k/nt) - 1]
            res.append(val)
            t = nt
            k %= nt
            ODD.remove(val)
        else:
            t = perm(len(EVEN), len(EVEN)) ** 2 * 2
            if k > t: return []
            nt  = t // n
            val = A[ceil(k/nt) - 1]
            res.append(val)
            t = nt
            k %= nt
            if val&1:
                ODD.remove(val)
            else:
                EVEN.remove(val)

        for i in range(2,n+1):
            if val&1:
                nt = t//len(EVEN)
                val = EVEN[ceil(k/nt) - 1]
                EVEN.remove(val)
            else:
                nt = t//len(ODD)
                val = ODD[ceil(k/nt) - 1]
                ODD.remove(val)
            res.append(val)
            t = nt
            k %= nt
        return res
