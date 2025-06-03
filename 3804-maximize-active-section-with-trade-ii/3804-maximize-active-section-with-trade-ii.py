class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.max_tree = [-math.inf] * self.n
        self.max_tree.extend(arr)
        for i in range(self.n - 1, 0, -1):
            self.max_tree[i] = max(self.max_tree[i << 1], self.max_tree[i << 1 | 1])

    def update(self, i, inc):
        i += self.n
        self.max_tree[i] += inc
        while i > 1:
            self.max_tree[i >> 1] = max(self.max_tree[i], self.max_tree[i ^ 1])
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
        return maximum if maximum > -inf else 0
    
    def print(self):
        for i in range(self.n):
            print(self.max_val(i,i+1), end=' ')
        print()

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        N = len(s)
        A = []
        i = 0
        no1 = 0
        while i < N:
            j = i+1
            while j < N and s[i] == s[j]:
                j += 1
            if s[i] == '0':
                A.append([i, j-1])
            else:
                no1 += j-i
            i = j
        if not A: return [no1] * len(queries)
        T = SegmentTree([0]*(len(A)))
        # 0000 111 00  1111 0000
        # 0-3  4-6 7-8 9-12 13-16
        # 0-3   7-8  13-16
        # print(A)
        for i in range(len(A)-1):
            d = A[i][1] - A[i][0] + 1 + A[i+1][1] - A[i+1][0] + 1
            T.update(i, d)
        res = []
        def update(i, d):
            if d == 0: return
            T.update(i, d)
            if i-1 >= 0:
                T.update(i-1, d)
        # T.print()
        for a,b in queries:
            i = bisect_right(A, a, key=lambda x:x[0])
            l = i
            old_l = new_l = 0
            if i and A[i-1][0] <= a <= A[i-1][1]:
                old_l = A[i-1][1] - A[i-1][0] + 1
                new_l = A[i-1][1] - a + 1
                l = i-1
                update(l, new_l - old_l)
            
            i = bisect_right(A, b, key=lambda x:x[0])
            r = i-1
            old_r = new_r = 0
            if i and A[i-1][0] <= b <= A[i-1][1]:
                old_r = A[i-1][1] - A[i-1][0] + 1
                new_r = b - A[i-1][0] + 1
                r = i-1
                update(r, new_r - old_r)
            # T.print()
            # print('l,r', l,r)
            res.append(no1 + T.max_val(l, r))
            update(l, old_l - new_l)
            update(r, old_r - new_r)
            
        return res