class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        mp = Counter(nums)
        A = sorted(mp.keys())
        p_cnt = mp[A[0]]
        d = 0
        j = 0
        res = p_cnt
        for i in range(1, len(A)):
            d += p_cnt*(A[i] - A[i-1])
            p_cnt += mp[A[i]]
            while d > k:
                x = min(mp[A[j]], ceil((d-k)/(A[i] - A[j])))
                mp[A[j]] -= x
                p_cnt -= x
                d -= x*(A[i] - A[j])
                if mp[A[j]] == 0:
                    j += 1
            res = max(res, p_cnt)
        return res