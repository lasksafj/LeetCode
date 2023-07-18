class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        A = [0]*n
        for a,b in roads:
            A[a] += 1
            A[b] += 1
        A.sort()
        return sum([(i+1)*A[i] for i in range(n)])
        