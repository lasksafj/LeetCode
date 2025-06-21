class Solution:
    def minimizeResult(self, expression: str) -> str:
        res = [0,0,inf]
        A,B = expression.split('+')
        for i in range(len(A)):
            if i == 0:
                l = 1
            else:
                l = int(A[:i])
            a = int(A[i:])
            for j in range(len(B)):
                b = int(B[:j+1])
                if j+1 == len(B):
                    r = 1
                else:
                    r = int(B[j+1:])
                res = min(res, [i,j,(a+b)*l*r], key=lambda x:x[2])
        i,j = res[:2]
        return A[:i] + '(' + A[i:] + '+' + B[:j+1] + ')' + B[j+1:]