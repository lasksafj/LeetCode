class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        cur = 0
        res = []
        sa = set()
        sb = set()
        for a,b in zip(A,B):
            if a in sb:
                cur += 1
            if b in sa:
                cur += 1
            if a == b:
                cur += 1
            sa.add(a)
            sb.add(b)
            res.append(cur)
        return res