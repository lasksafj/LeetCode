class Solution:
    def maximum69Number (self, num: int) -> int:
        A = list(str(num))
        try:
            p = A.index('6')
        except:
            p = -1
        if p >= 0:
            A[p] = '9'
        return int(''.join(A))