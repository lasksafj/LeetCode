class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        for i in range(len(citations)-1, -1, -1):
            h += 1
            a = citations[i-1] if i > 0 else 0
            if a <= h and h <= citations[i]:
                return h
        return citations[0]