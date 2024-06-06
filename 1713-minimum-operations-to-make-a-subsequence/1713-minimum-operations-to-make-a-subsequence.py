class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        mp = {}
        for i,t in enumerate(target):
            mp[t] = i
        A = []
        for a in arr:
            if a in mp:
                b = mp[a]
                p = bisect_left(A, b)
                if p == len(A):
                    A.append(b)
                else:
                    A[p] = b
        return max(0, len(target) - len(A))