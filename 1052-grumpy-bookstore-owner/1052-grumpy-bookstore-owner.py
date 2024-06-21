class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        N = len(customers)
        pre = list(accumulate(customers, initial=0))
        @cache
        def dfs(i, use):
            if i >= N:
                return 0
            res = dfs(i+1, use) + (customers[i] if grumpy[i] == 0 else 0)
            if use:
                res = max(res, dfs(i+minutes, 0) + pre[min(N,i+minutes)]-pre[i])
            return res
        return dfs(0,1)