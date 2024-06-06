class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        from sortedcontainers import SortedList
        mp = {}
        for i,t in enumerate(target):
            mp[t] = i
        A = SortedList()
        for a in arr:
            if a in mp:
                b = mp[a]
                p = A.bisect_left(b)
                if p < len(A):
                    del A[p]
                A.add(b)
        return max(0, len(target) - len(A))