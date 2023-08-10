class Solution:
    def maximumSwap(self, num: int) -> int:
        A = list(str(num))
        N = len(A)
        for i in range(N-1):
            if A[i] < '9':
                ma = A[i+1]
                midx = i+1
                for j in range(i+2,N):
                    if A[j] >= ma:
                        ma = A[j]
                        midx = j
                if ma > A[i]:
                    A[i],A[midx] = A[midx],A[i]
                    return int(''.join(A))
            # print(A)
        return num