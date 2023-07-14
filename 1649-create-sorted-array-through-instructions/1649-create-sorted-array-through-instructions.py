class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        from sortedcontainers import SortedList
        mod = 10**9+7
        A = SortedList()
        res = 0
        for n in instructions:
            res = (res + min(A.bisect_left(n), len(A) - A.bisect_right(n))) % mod
            A.add(n)
        return res