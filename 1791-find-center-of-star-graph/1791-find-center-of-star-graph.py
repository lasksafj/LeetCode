class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        ind = defaultdict(int)
        for a,b in edges:
            ind[a] += 1
            ind[b] += 1
            if ind[a] > 1:
                return a
            if ind[b] > 1:
                return b
        return -1
            