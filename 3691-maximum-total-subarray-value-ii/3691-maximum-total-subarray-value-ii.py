class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.max_tree = [-math.inf] * self.n
        self.max_tree.extend(arr)
        self.min_tree = [math.inf] * self.n
        self.min_tree.extend(arr)
        for i in range(self.n - 1, 0, -1):
            self.max_tree[i] = max(self.max_tree[i << 1], self.max_tree[i << 1 | 1])
            self.min_tree[i] = min(self.min_tree[i << 1], self.min_tree[i << 1 | 1])

    def update(self, i, val):
        i += self.n
        self.max_tree[i] = val
        self.min_tree[i] = val
        while i > 1:
            self.max_tree[i >> 1] = max(self.max_tree[i], self.max_tree[i ^ 1])
            self.min_tree[i >> 1] = min(self.min_tree[i], self.min_tree[i ^ 1])
            i >>= 1

    def max_val(self, l, r):
        maximum = -math.inf
        l += self.n
        r += self.n
        while l < r:
            if (l & 1):
                maximum = max(maximum, self.max_tree[l])
                l += 1
            if (r & 1):
                r -= 1
                maximum = max(maximum, self.max_tree[r])
            l >>= 1
            r >>= 1
        return maximum

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
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        N = len(nums)
        T = SegmentTree(nums)
        def val(l,r): return T.max_val(l,r) - T.min_val(l,r)
        pq = []
        for i in range(len(nums)):
            heappush(pq, [-val(i,N), i,N])
        res = 0
        while k:
            v,l,r = heappop(pq)
            v = -v
            res += v
            r -= 1
            heappush(pq, [-val(l,r), l,r])
            k -= 1
        return res