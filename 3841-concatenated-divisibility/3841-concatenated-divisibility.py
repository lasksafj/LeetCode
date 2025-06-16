class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        N = len(nums)
        track = []
        @cache
        def dfs(mask,m):
            if mask == (1<<N)-1:
                return m == 0
            for j in range(N):
                if (1<<j)&mask:
                    continue
                a = nums[j]
                b = len(str(a))
                if dfs(mask^(1<<j), (m*(10**b) + a) % k):
                    track.append(nums[j])
                    return True
            return False
        dfs(0, 0)
        return track[::-1]