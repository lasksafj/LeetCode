class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        left = [[0]*2 for _ in range(n)]
        right = [[0]*2 for _ in range(n)]
        left[0][0] = 0+(customers[0] == 'N')
        left[0][1] = 0+(customers[0] == 'Y')
        for i in range(1,n):
            left[i][0] = left[i-1][0] + (customers[i] == 'N')
            left[i][1] = left[i-1][1] + (customers[i] == 'Y')
        right[-1][0] = 0+(customers[-1] == 'N')
        right[-1][1] = 0+(customers[-1] == 'Y')
        for i in range(n-2,-1,-1):
            right[i][0] = right[i+1][0] + (customers[i] == 'N')
            right[i][1] = right[i+1][1] + (customers[i] == 'Y')
        minpen = inf
        res = 0
        for i in range(n+1):
            cur = (left[i-1][0] if i>0 else 0) + (right[i][1] if i<n else 0)
            if minpen > cur:
                minpen = cur
                res = i
        return res