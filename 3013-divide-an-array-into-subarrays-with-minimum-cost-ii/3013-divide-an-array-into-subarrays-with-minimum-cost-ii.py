class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        k -= 2
        SL = SortedList(nums[1:1+dist])
        A = SortedList(SL[:k])
        B = SortedList(SL[k:])
        s = sum(A)
        res = inf
        for i in range(1, len(nums)-k):
            n = nums[i]
            if n in B:
                B.remove(n)
            else:
                A.remove(n)
                s -= n
                if B:
                    s += B[0]
                    A.add(B.pop(0))
            if i+dist < len(nums):
                B.add(nums[i+dist])
                if len(A) < k:
                    s += B[0]
                    A.add(B.pop(0))
                elif A[-1] > B[0]:
                    s = s - A[-1] + B[0]
                    a,b = A.pop(),B.pop(0)
                    A.add(b)
                    B.add(a)
            res = min(res, nums[0] + n + s)
        return res