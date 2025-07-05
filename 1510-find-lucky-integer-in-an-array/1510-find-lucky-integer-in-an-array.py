class Solution:
    def findLucky(self, arr: List[int]) -> int:
        for a,b in sorted(Counter(arr).items(), reverse=1):
            if a == b:
                return a
        return -1