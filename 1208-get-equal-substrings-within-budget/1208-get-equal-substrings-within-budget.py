class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        A = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        j = 0
        res = 0
        cost = 0
        for i in range(len(A)):
            cost += A[i]
            while j <= i and cost > maxCost:
                cost -= A[j]
                j += 1
            res = max(res, i-j+1)
        return res