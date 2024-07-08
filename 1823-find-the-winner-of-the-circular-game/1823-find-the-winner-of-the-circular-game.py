class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i = 0
        d = 0
        A = [1]*n
        while d < n-1:
            cnt = 0
            while cnt < k-1:
                if A[i]:
                    cnt += 1
                i = (i+1)%n
            while A[i] == 0:
                i = (i+1)%n
            A[i] = 0
            while A[i] == 0:
                i = (i+1)%n
            d += 1
        return i+1