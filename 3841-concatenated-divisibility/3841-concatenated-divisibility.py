class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        N = len(nums)
        track = [-1]*N
        @cache
        def dfs(i,mask,m):
            if i == N:
                return m == 0
            for j in range(N):
                if (1<<j)&mask:
                    continue
                a = nums[j]
                b = len(str(a))
                if dfs(i+1, mask^(1<<j), (m*(10**b) + a) % k):
                    track[i] = nums[j]
                    return True
            return False
        dfs(0, 0, 0)
        return track if track[0] >= 0 else []