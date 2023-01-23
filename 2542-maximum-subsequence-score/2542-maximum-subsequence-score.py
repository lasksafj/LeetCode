class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        res = 0
        p = sorted([i for i in range(n)], key=lambda x:-nums2[x])
        s = 0
        pq = []
        for i in p:
            if len(pq) == k:
                s -= heapq.heappop(pq)
            s += nums1[i]
            heapq.heappush(pq, nums1[i])
            if len(pq) == k:
                res = max(res, nums2[i] * s)
        return res
                
            
            