class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        is_sorted = [0]*len(strs)
        for j in range(len(strs[0])):
            ok = True
            is_sorted2 = is_sorted[:]
            for i in range(len(strs)-1):
                if strs[i][j] > strs[i+1][j] and is_sorted[i] == 0:
                    res += 1
                    ok = False
                    break
                if strs[i][j] < strs[i+1][j]:
                    is_sorted2[i] = 1
            if ok:
                is_sorted = is_sorted2[:]
        return res