class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        A = sorted(Counter(arr).values())
        for i,n in enumerate(A):
            k -= n
            if k < 0:
                return len(A) - i
        return 0