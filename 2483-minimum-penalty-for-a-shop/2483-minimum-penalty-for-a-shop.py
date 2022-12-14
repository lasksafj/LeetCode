class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        left = [0]*n
        right = [0]*n
        left[0] = 0+(customers[0] == 'N')
        for i in range(1,n):
            left[i] = left[i-1] + (customers[i] == 'N')
        right[-1] = 0+(customers[-1] == 'Y')
        for i in range(n-2,-1,-1):
            right[i] = right[i+1] + (customers[i] == 'Y')
        minpen = inf
        res = 0
        for i in range(n+1):
            cur = (left[i-1] if i>0 else 0) + (right[i] if i<n else 0)
            if minpen > cur:
                minpen = cur
                res = i
        return res