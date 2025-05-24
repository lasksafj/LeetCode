# increment range, query sum
class SegTree:
    def __init__(self, left, right, nums) -> None:
        self.left = left
        self.right = right
        self.lazy = 0
        if left == right:
            self.val = nums[left]
        else:
            mi = (left + right)//2
            self.lchild = SegTree(left, mi, nums)
            self.rchild = SegTree(mi+1, right, nums)
            self.calc()
    
    def calc(self):
        if self.left == self.right:
            return
        self.val = self.lchild.val + self.rchild.val

    def propogate(self):
        if self.lazy == 0:
            return
        self.val += (self.right - self.left + 1) * self.lazy
        if self.left < self.right:
            self.lchild.lazy += self.lazy
            self.rchild.lazy += self.lazy
        self.lazy = 0
    
    def update(self, l, r, inc):
        self.propogate()
        if l > self.right or r < self.left:
            return
        if l <= self.left and self.right <= r:
            self.lazy += inc
            self.propogate()
            return
        self.lchild.update(l, r, inc)
        self.rchild.update(l, r, inc)
        self.calc()
    
    def query(self, l, r):
        self.propogate()
        if l > self.right or r < self.left:
            return 0
        if l <= self.left and self.right <= r:
            return self.val
        return self.lchild.query(l, r) + self.rchild.query(l, r)
    
    def __repr__(self):
        return "SegmentTree({0})".format([self.range_sum(i,i) for i in range(self.right+1)])

class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a,b,w in edges:
            adj[a].append([b,w])
            adj[b].append([a,w])
        timer = 0
        tin = [0]*(n+1)
        tout = [0]*(n+1)

        dist = [0]*(n+1)
        val = [0]*(n+1)
        flat = [0]
        def dfs(i,p, d):
            nonlocal timer
            timer += 1
            tin[i] = timer
            dist[i] = d
            flat.append(i)
            for ne,w in adj[i]:
                if ne == p: continue
                val[ne] = w
                dfs(ne, i, d+w)
            tout[i] = timer
        dfs(1, 0, 0)

        flat_dist = [dist[i] for i in flat]
        T = SegTree(0, n, flat_dist)

        res = []
        for q in queries:
            if q[0] == 1:
                _,u,v,w = q
                if tin[u] > tin[v]:
                    u,v = v,u
                inc = w - val[v]
                val[v] = w
                T.update(tin[v], tout[v], inc)
            else:
                _,u = q
                res.append(T.query(tin[u], tin[u]))
        return res