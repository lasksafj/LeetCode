class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        pre = list(accumulate(stoneValue, initial=0))
        # print(pre)
        def sum_(i,j):
            return pre[j+1]-pre[i]
        @cache
        def best_left(i,j):
            if i > j:
                return -inf
            if i==j:
                return stoneValue[i]
            return max(best_left(i,j-1), dfs(i,j) + sum_(i,j))
        @cache
        def best_right(i,j):
            if i > j:
                return -inf
            if i==j:
                return stoneValue[i]
            return max(best_right(i+1,j), dfs(i,j) + sum_(i,j))
        
        @cache
        def dfs(i,j):
            if i==j:
                return 0       
            res = 0
            mi = (pre[j+1]+pre[i])//2
            k = bisect_right(pre, mi)-1
            
            
            l = sum_(i,k-1)
            r = sum_(k,j)
            if l < r:
                res = max(res, best_left(i,k-1)) 
            elif l > r:
                res = max(res, best_right(k,j))
            else:
                res = max(res, best_left(i,k-1), best_right(k,j))
            if k+1 <= j:
                res = max(res, best_right(k+1,j))
            
            # print(i,k,j,'res',res)
            return res
            
        return dfs(0,len(stoneValue)-1)