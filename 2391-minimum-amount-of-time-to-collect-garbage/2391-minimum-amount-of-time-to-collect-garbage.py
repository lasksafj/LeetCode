class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        rg,rp,rm = 0,0,0
        dg,dp,dm = 0,0,0
        travel.append(0)
        for i,w in enumerate(garbage):
            if 'G' in w:
                rg += dg + w.count('G')
                dg = travel[i]
            else:
                dg += travel[i]
            if 'P' in w:
                rp += dp + w.count('P')
                dp = travel[i]
            else:
                dp += travel[i]
            if 'M' in w:
                rm += dm + w.count('M')
                dm = travel[i]
            else:
                dm += travel[i]
        # print(rg,rp,rm)
        return rg+rp+rm