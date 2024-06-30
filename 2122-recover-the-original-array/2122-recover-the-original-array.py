class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        nums.sort()
        a = nums[0]
        for n in nums[1:]:
            tmp = cnt.copy()
            if (n-a)%2 == 0:
                k = (n-a)//2
                if k == 0:
                    continue
                res = []
                for n in nums:
                    if n in tmp and n+k*2 in tmp:
                        tmp[n] -= 1
                        tmp[n+k*2] -= 1
                        if tmp[n] == 0:
                            del tmp[n]
                        if tmp[n+k*2] == 0:
                            del tmp[n+k*2]
                        res.append(n+k)
                if len(res)*2 == len(nums) and len(tmp) == 0:
                    return res
        return []