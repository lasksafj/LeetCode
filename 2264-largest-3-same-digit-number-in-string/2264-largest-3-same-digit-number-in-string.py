class Solution:
    def largestGoodInteger(self, num: str) -> str:
        N = len(num)
        i = 0
        res = -1
        while i < N:
            j = i
            while j+1 < N and num[j] == num[j+1]:
                j += 1
            if j-i >= 2:
                res = max(res, int(num[i]))
            i = j+1
        return str(res)*3 if res > -1 else ""