class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.min_tree = [math.inf] * self.n
        self.min_tree.extend(arr)
        for i in range(self.n - 1, 0, -1):
            self.min_tree[i] = min(self.min_tree[i << 1], self.min_tree[i << 1 | 1])

    def update(self, i, val):
        i += self.n
        self.min_tree[i] = val
        while i > 1:
            self.min_tree[i >> 1] = min(self.min_tree[i], self.min_tree[i ^ 1])
            i >>= 1

    def min_val(self, l, r):
        minimum = math.inf
        l += self.n
        r += self.n
        while l < r:
            if (l & 1):
                minimum = min(minimum, self.min_tree[l])
                l += 1
            if (r & 1):
                r -= 1
                minimum = min(minimum, self.min_tree[r])
            l >>= 1
            r >>= 1
        return minimum

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        sorted_nums1 = sorted(set(nums1))
        def idx_sorted_nums1(n):
            return bisect_left(sorted_nums1, n)
        T = SegmentTree([inf]*len(sorted_nums1))
        res = 0
        for i in range(len(nums1)):
            a = nums1[i]
            k = idx_sorted_nums1(a)
            if T.min_val(k,k+1) > i:
                T.update(k, i)
        for i in range(len(nums2)):
            b = nums2[i]
            if b < sorted_nums1[0]: continue
            q = bisect_right(sorted_nums1, b)
            res = max(res, i-T.min_val(0, q))
        return res