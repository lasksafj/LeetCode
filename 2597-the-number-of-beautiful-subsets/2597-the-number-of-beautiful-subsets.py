class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        m = {}
        res = [0]
        def sol(i):
            for j in range(i+1,len(nums)):
                a = nums[j]-k
                if a not in m:
                    if nums[j] not in m:
                        m[nums[j]] = 1
                    else:
                        m[nums[j]] += 1
                    sol(j)
                    m[nums[j]] -= 1
                    if m[nums[j]] == 0:
                        del m[nums[j]]
            if len(m) > 0:
                res[0] += 1
        sol(-1)
        return res[0]