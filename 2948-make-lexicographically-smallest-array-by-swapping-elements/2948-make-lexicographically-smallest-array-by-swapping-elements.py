class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        A = sorted(nums)
        p = -inf
        B = []
        mp = {}
        for a in A:
            if a-limit > p:
                B.append(deque())
            B[-1].append(a)
            mp[a] = len(B)-1
            p = a
        res = []
        for n in nums:
            res.append(B[mp[n]].popleft())
        return res