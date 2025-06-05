class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        N = len(nums)
        
        A,B = SortedList(),SortedList()
        sa,sb = 0,0
        def balance():
            nonlocal sa,sb,A,B
            if len(B) > len(A):
                b = B.pop(0)
                sb -= b
                A.add(b)
                sa += b
            elif len(B) < len(A)-1:
                a = A.pop(-1)
                sa -= a
                B.add(a)
                sb += a
        def add(d):
            nonlocal sa,sb,A,B
            if not A or d <= A[-1]:
                A.add(d)
                sa += d
            else:
                B.add(d)
                sb += d
            balance()
        def remove(d):
            nonlocal sa,sb,A,B
            if d in A:
                A.remove(d)
                sa -= d
            else:
                B.remove(d)
                sb -= d
            balance()

        C = [0]*N
        for i in range(N):
            add(nums[i])
            if i >= x:
                remove(nums[i-x])
            if i >= x-1:
                C[i] = A[-1]*len(A) - sa + sb - A[-1]*len(B)
            
        dp = [[inf]*(N+1) for _ in range(k+1)]
        dp[0] = [0]*(N+1)
        for t in range(1, k+1):
            for i in range(x*t, N+1):
                dp[t][i] = min(dp[t][i-1], dp[t-1][i-x] + C[i-1])
        return dp[k][-1]