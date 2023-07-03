class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        m = defaultdict(int)
        j = 0
        for i in range(n):
            m[nums[i]] += 1
            while j < i and max(m) - min(m) > 2:
                m[nums[j]] -= 1
                if m[nums[j]] == 0:
                    del m[nums[j]]
                j += 1
            res += i-j+1
        return res