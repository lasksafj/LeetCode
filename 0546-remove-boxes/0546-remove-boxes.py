class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        #dp: maximum value of removing boxes if we have k extra boxes of color A[i] to the left of A[i:j+1]
        @cache
        def dp(l,r,k):
            if l > r:
                return 0
            while l<r and boxes[l] == boxes[l+1]:
                l += 1
                k += 1
            res = dp(l+1,r,0) + (k+1)*(k+1)
            for mi in range(l+1,r+1):
                if boxes[l] == boxes[mi]:
                    res = max(res, dp(mi,r,k+1) + dp(l+1,mi-1,0))
            return res
        return dp(0,len(boxes)-1,0)