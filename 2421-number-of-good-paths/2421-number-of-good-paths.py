class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        def f(x):
            while x != p[x]:
                x = p[x]
            return x
        
        edges.sort(key=lambda x: max(vals[x[0]], vals[x[1]]))
        vals = [[x,1] for x in vals]
        rank = [0] * len(vals)
        # print(edges)
        p = [i for i in range(len(vals))]
        res = len(vals)
        for a,b in edges:
            y1,y2 = f(a), f(b)
            if y1 == y2:
                continue
            m1,n1 = vals[y1]
            m2,n2 = vals[y2]
            if rank[y1] > rank[y2]:
                p[y2] = y1
                yf = y1
            elif rank[y1] < rank[y2]:
                p[y1] = y2
                yf = y2
            else:
                p[y1] = y2
                yf = y2
                rank[y2] += 1
            if m1 == m2:
                res += n1 * n2
                vals[yf][1] = n1 + n2
            else:
                vals[yf][1] = n1 if m1 > m2 else n2
                vals[yf][0] = max(m1,m2)
            # print(a,b,'----',yf,res)
                
        return res