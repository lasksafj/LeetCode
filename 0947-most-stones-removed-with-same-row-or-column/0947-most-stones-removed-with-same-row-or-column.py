class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        f = {}
        
        def find(a):
            if a not in f:
                f[a] = a
            if f[a] == a:
                return a
            return find(f[a])
        
        def union(a, b):
            x,y = find(a),find(b)
            if x != y:
                f[y] = x
                
        for stone in stones:
            union(stone[0], ~stone[1])
        no_group = 0
        for x in f:
            if find(x) == x:
                no_group += 1
        return n - no_group
                    