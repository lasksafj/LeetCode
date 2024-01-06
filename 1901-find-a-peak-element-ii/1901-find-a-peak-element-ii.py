class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        M,N = len(mat),len(mat[0])
        # for r in mat:
        #     print(r)
        l,r = 0,M
        while l < r:
            mi = (l+r)//2
            
            top = max(mat[mi-1]) if mi>0 else -1
            bot = max(mat[mi+1]) if mi+1<M else -1
            cur = max(mat[mi])
            ma = max(top,cur,bot)
            
            # print(mi,top,cur,bot)
            
            
            if cur == ma:
                return [mi, mat[mi].index(max(mat[mi]))]
            if top == ma:
                r = mi
            else:
                l = mi+1
            
        return [-1,-1]