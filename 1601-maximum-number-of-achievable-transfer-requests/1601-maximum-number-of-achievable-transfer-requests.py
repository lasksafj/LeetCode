class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def check(A):
            for n in A:
                if n != 0:
                    return False
            return True
        A = [0]*n
        res = [0]
        # for a,b in requests:
        #     A[a] -= 1
        #     A[b] += 1
        
        def dfs(i, noreq, A):
            # print(i,noreq, A)
            if i == len(requests):
                if check(A):
                    res[0] = max(res[0], noreq)
                return
            
            a,b = requests[i]
            A[a] -= 1
            A[b] += 1
            dfs(i+1, noreq+1, A)
            A[a] += 1
            A[b] -= 1
            dfs(i+1, noreq, A)
        
        dfs(0,0,A)
        return res[0]