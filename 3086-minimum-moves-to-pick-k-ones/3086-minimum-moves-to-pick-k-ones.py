class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        A = [i for i,n in enumerate(nums) if n == 1]
        N = len(A)
        pre = list(accumulate(A, initial=0))
        res = inf
        step2 = max(0, k-maxChanges)
        
        for m in range(step2, min(k,step2+3,N)+1):
            for i in range(N-m+1):
                #step 2 takes 1 action
                d = pre[i+m]-pre[i+m-m//2] - (pre[i+m//2]-pre[i])
                
                #step 1 takes 2 actions
                res = min(res, d+(k-m)*2)
        return res