class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        p = sorted(list(range(n)), key=lambda x:-nums2[x] )
        res = 0
        pq = []
        s = 0
        for i in range(n):
            s += nums1[p[i]]
            heappush(pq, nums1[p[i]])
            if len(pq) > k:
                s -= heappop(pq)
            if len(pq) == k:
                res = max(res,s*nums2[p[i]])
        return res
            