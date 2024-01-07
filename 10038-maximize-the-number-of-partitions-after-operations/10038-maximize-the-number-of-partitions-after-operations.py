class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @cache
        def dfs(i,change,mask):
            if i == len(s):
                return 1
            d = ord(s[i]) - ord('a')
            mask2 = mask|(1<<d)
            cnt = mask2.bit_count()
            if cnt > k:
                res = dfs(i+1,change,1<<d) + 1
            else:
                res = dfs(i+1,change,mask2)
            if change:
                for j in range(26):
                    mask2 = mask|(1<<j)
                    cnt = mask2.bit_count()
                    if cnt > k:
                        res = max(res, dfs(i+1,0,1<<j) + 1)
                    else:
                        res = max(res, dfs(i+1,0,mask2))
            return res
        
        return dfs(0,1,0)