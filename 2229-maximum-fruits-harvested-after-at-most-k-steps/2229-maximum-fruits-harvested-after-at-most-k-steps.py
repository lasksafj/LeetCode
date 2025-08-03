class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        pre = [fruits[0][1]]
        for _,f in fruits[1:]:
            pre.append(pre[-1] + f)
        pre.append(pre[-1])
        res = 0
        for i,(p,f) in enumerate(fruits):
            l = max(0, startPos - p)
            r = k - 2*l
            if r < 0: continue
            j = bisect_right(fruits, startPos+r, key=lambda x:x[0])-1
            if j > -1:
                res = max(res, pre[j] - (pre[i-1] if i else 0))
        for j in range(len(fruits)-1,-1,-1):
            p = fruits[j][0]
            r = max(0, p - startPos)
            l = k - 2*r
            if l < 0: continue
            i = bisect_left(fruits, startPos-l, key=lambda x:x[0])
            res = max(res, pre[j] - (pre[i-1] if i else 0))
        return res