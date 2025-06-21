class Solution:
    def solveEquation(self, equation: str) -> str:
        A,B = equation.split('=')
        def f(A):
            x = d = 0
            i = 0
            N = len(A)
            while i < N:
                j = i
                if A[j] in '+-':
                    j += 1
                while j < N and A[j].isdigit():
                    j += 1
                try:
                    n = int(A[i:j])
                except:
                    n = 1
                    if A[i] == '-':
                        n = -1
                if j < N and A[j] == 'x':
                    x += n
                    i = j+1
                else:
                    d += n
                    i = j
            return x,d
        x1,d1 = f(A)
        x2,d2 = f(B)
        if x1 == x2 and d1 == d2:
            return 'Infinite solutions'
        elif x1 == x2 and d1 != d2:
            return 'No solution'
        res = (d2-d1)//(x1-x2)
        return 'x=' + str(res)