class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        cur = 0
        for n in arr:
            if n <= cur:
                cur = n
            else:
                cur += 1
        return cur