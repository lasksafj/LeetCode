from sortedcontainers import SortedSet
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        N = len(stones)
        def check(x):
            A = [1]*N
            prev = stones[0]
            i = 1
            while i < N:
                if stones[i]-prev > x:
                    prev = stones[i-1]
                    A[i-1] = 0
                    if stones[i]-prev > x:
                        return False
                i += 1
            i = N-1
            prev = stones[N-1]
            prev_i = N-1
            # print('---',A)
            while i >= 0:
                if A[i] == 0:
                    i -= 1
                    continue
                if prev-stones[i] > x:
                    prev = stones[prev_i]
                    if prev-stones[i] > x:
                        return False
                prev_i = i
                i -= 1
            return True
        l,r = 1, stones[-1] - stones[0]
        while l <= r:
            mi = (l+r)//2
            # print(mi)
            if check(mi):
                r = mi-1
            else:
                l = mi+1
        return l