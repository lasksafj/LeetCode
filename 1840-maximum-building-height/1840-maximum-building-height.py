class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.sort()
        # print(restrictions)
        prev_h = 0
        prev_i = 1
        A = []
        for i,h in restrictions:
            A.append([i,min(h, i-prev_i+prev_h)])
            prev_i,prev_h = A[-1]
        # print(A)
        prev_h = inf
        prev_i = n
        for j in range(len(A)-1,-1,-1):
            i,h = A[j]
            A[j][1] = min(h, prev_i-i+prev_h)
            prev_i,prev_h = A[j]
            
        # print(A)
        
        prev_h = 0
        prev_i = 1
        res = 0
        for i,h in A:
            x = (i-prev_i + (prev_h+h))//2
            res = max(res, x)
            prev_i,prev_h = i,h
        return max(res, prev_h+n-prev_i)