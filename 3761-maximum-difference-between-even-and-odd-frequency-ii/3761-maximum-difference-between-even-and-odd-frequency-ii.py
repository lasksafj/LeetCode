class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        N = len(s)
        res = -inf
        for a,b in permutations('01234', 2):
            mp = {}
            mp[0] = [0,0,0]
            cnta = cntb = 0
            pcnta = pcntb = 0
            for i in range(N):
                if i-k >= 0:
                    pcnta += s[i-k] == a
                    pcntb += s[i-k] == b
                    pmask = ((pcnta&1)<<1) | (pcntb&1)
                    pcur = pcnta - pcntb
                    if pmask in mp:
                        mp[pmask] = min(mp[pmask], [pcur, pcnta, pcntb], key=lambda x: x[0])
                    else:
                        mp[pmask] = [pcur,pcnta,pcntb]
                cnta += s[i] == a
                cntb += s[i] == b
                mask = ((cnta&1)<<1) | (cntb&1)
                if i+1 >= k and mask^2 in mp:
                    cur = cnta - cntb
                    d, ca,cb = mp[mask^2]
                    if cnta-ca and cntb-cb:
                        res = max(res, cur - d)
        return res