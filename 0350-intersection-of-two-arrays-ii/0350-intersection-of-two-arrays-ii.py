class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt = Counter(nums1)
        res = []
        for n in nums2:
            if cnt[n] > 0:
                res.append(n)
                cnt[n] -= 1
        return res