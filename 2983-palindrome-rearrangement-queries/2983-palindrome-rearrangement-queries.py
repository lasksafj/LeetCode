def cover(i1,j1,i2,j2,tA,tB):
    # print(i1,j1,i2,j2)
    for ch in string.ascii_lowercase:
        if tA[ch][j1] - tA[ch][i1-1] < tB[ch][j2] - tB[ch][i2-1]:
            # print('---',ch)
            return False
    return True

class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        N = len(s)
        mA = defaultdict(lambda:defaultdict(int))
        mB = defaultdict(lambda:defaultdict(int))
        A = s[:N//2]
        B = s[N//2:][::-1]
        for i in range(N//2):
            for ch in string.ascii_lowercase:
                mA[ch][i] = mA[ch][i-1] + (A[i] == ch)
                mB[ch][i] = mB[ch][i-1] + (B[i] == ch)
        
        bad = []
        for i in range(N//2):
            if s[i] != s[N-i-1]:
                bad.append(i)
        if len(bad) == 0:
            return [True]*len(queries)
        
        res = []
        for a,b,c,d in queries:
            i1,j1 = a,b
            i2,j2 = N-d-1,N-c-1
            if (i1 > bad[0] and i2 > bad[0]) or (j1 < bad[-1] and j2 < bad[-1]) \
            or (i1 > bad[-1] and i2 > bad[-1]) or (j1 < bad[0] and j2 < bad[0]):
                res.append(False)
                continue
            
            if i2 < i1:
                tA,tB = mB,mA
                i1,i2 = i2,i1
                j1,j2 = j2,j1
            else:
                tA,tB = mA,mB
            
            if i2 > j1:
                p = bisect_right(bad, j1)
                if p < len(bad) and bad[p] < i2:
                    res.append(False)
                    continue
                r = cover(i1,j1,i1,j1,tA,tB) & cover(i2,j2,i2,j2,tB,tA)
                res.append(r)
                continue
            if j2 <= j1:
                r = cover(i1,j1,i1,j1,tA,tB)
                res.append(r)
                continue
            # print(i1,j1,i2,j2)
            # print(B)
            # print(A)
            # print(cover(i1,j1,i1,i2-1,tA,tB))
            # print( cover(i2,j2,j1,j2-1,tB,tA) )
            # print( cover(i1,j2,i1,j2,tA,tB) )
            r = cover(i1,j1,i1,i2-1,tA,tB) & cover(i2,j2,j1+1,j2,tB,tA) & cover(i1,j2,i1,j2,tA,tB)
            res.append(r)
                        
        return res