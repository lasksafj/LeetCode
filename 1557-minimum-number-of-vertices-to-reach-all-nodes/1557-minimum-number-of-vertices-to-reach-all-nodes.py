class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = set(range(n))
        for a,b in edges:
            if b in res:
                res.remove(b)
        return res