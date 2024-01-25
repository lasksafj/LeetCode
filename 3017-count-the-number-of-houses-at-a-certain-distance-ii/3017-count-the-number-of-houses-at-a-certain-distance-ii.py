class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x > y:
            x,y = y,x
        A = [0]*(n+1)
        for i in range(1,n+1):
            A[1] += 2   # update range 1...n
            A[min(i-1, abs(i-y)+1+x-1) + 1] -= 1
            A[min(n-i, abs(i-x)+1+n-y) + 1] -= 1
            A[min(abs(i-x), abs(i-y)+1) + 1] += 1
            A[min(abs(i-y), abs(i-x)+1) + 1] += 1
            r = max(x-i, 0) + max(i-y, 0)
            A[r + (y-x)//2 + 1] -= 1
            A[r + (y-x+1)//2 + 1] -= 1
        for i in range(2,n+1):
            A[i] += A[i-1]
        return A[1:]
            