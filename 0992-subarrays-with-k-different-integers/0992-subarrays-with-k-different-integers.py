class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def nosubarray_less_or_equal(x):
            res = 0
            m = defaultdict(int)
            j = 0
            l = 0
            for i in range(len(nums)):
                m[nums[i]] += 1
                if m[nums[i]] == 1:
                    l += 1
                while j <= i and l > x:
                    m[nums[j]] -= 1
                    if m[nums[j]] == 0:
                        l -= 1
                    j += 1
                res += i-j+1
            return res
        return nosubarray_less_or_equal(k) - nosubarray_less_or_equal(k-1)