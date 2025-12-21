class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        N = len(strs)
        res = 0
        A = [1]*(N-1)
        for j in range(len(strs[0])):
            ok = True
            for i in range(N-1):
                if A[i] and strs[i][j] > strs[i+1][j]:
                    res += 1
                    ok = False
                    break
            if ok:
                for i in range(N-1):
                    if A[i] and strs[i][j] < strs[i+1][j]:
                        A[i] = 0
        return res