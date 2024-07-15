class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if restrictions == []:
            return n-1
        A = sorted(restrictions)
        
        res = inf
        st = [[1,0]]
        for i,h in A:
            cur_res = 0
            while st and h < st[-1][1] - (i-st[-1][0]):
                st.pop()
            if not st or i-st[-1][0] + st[-1][1] >= h:
                st.append([i,h])
        
        res = 0
        for k in range(1,len(st)):
            li,lh = st[k-1]
            i,h = st[k]
            res = max(res, (h+lh+i-li)//2)
        return max(res, n-st[-1][0]+st[-1][1])