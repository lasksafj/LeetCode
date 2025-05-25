class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10:
            return n
        A = str(n)
        i = 0
        while i+1 < len(A) and A[i+1] >= A[i]:
            i += 1
        if i+1==len(A):
            return n
        i -= 1
        while i >= 0 and A[i] == A[i+1]:
            i -= 1
        return int(''.join(A[:i+1]) + str(int(A[i+1])-1) + '9' * (len(A)-(i+2)))