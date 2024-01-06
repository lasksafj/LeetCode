class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        l,r = 0,N
        while l < r:
            mi = (l+r)//2
            # print(mi)
            if citations[mi] >= N-mi:
                r = mi
            else:
                l = mi+1
        return N-l