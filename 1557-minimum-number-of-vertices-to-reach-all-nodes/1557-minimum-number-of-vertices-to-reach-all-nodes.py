class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = set()
        ind = defaultdict(int)
        for a,b in edges:
            ind[b] += 1
        for i in range(n):
            if ind[i] == 0:
                res.add(i)
        return res